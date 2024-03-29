from application.llm.base import BaseLLM
from application.core.settings import settings

class LlamaCpp(BaseLLM):

    def __init__(self, api_key, llm_name=settings.MODEL_PATH, **kwargs):
        global llama
        try:
            from llama_cpp import Llama
        except ImportError:
            raise ImportError("Please install llama_cpp using pip install llama-cpp-python")

        llama = Llama(model_path=llm_name, n_ctx=2048)

    def gen(self, model, engine, messages, stream=False, **kwargs):
        context = messages[0]['content']
        context = context[0:4000]
        user_question = messages[-1]['content']
        #prompt = f"### Instruction \n {user_question} \n ### Context \n {context} \n ### Answer \n"
        #prompt = f"[INST] <<SYS>> \n {context} \n <</SYS>> \n {user_question}[/INST] \n"
        prompt = f"<|im_start|>system \n {context}<|im_end|> \n <|im_start|>user \n {user_question}<|im_end|> \n <|im_start|>assistant\n"
        print("PROOOOOOOOOOOOOOOOOOOOOOOMT")
        print(len(prompt))
        result = llama(prompt, max_tokens=150, echo=False)

        # import sys
        # print(result['choices'][0]['text'].split('### Answer \n')[-1], file=sys.stderr)
        
        #return result['choices'][0]['text'].split('### Answer \n')[-1]
        return result['choices'][0]['text'].split('<|im_start|>assistant')[-1]

    def gen_stream(self, model, engine, messages, stream=True, **kwargs):
        context = messages[0]['content']
        user_question = messages[-1]['content']
        #prompt = f"### Instruction \n {user_question} \n ### Context \n {context} \n ### Answer \n"
        prompt = f"[INST] <<SYS>> \n {context} \n <</SYS>> \n {user_question}[/INST] \n"

        result = llama(prompt, max_tokens=150, echo=False, stream=stream)

        # import sys
        # print(list(result), file=sys.stderr)

        for item in result:
            for choice in item['choices']:
                yield choice['text']
