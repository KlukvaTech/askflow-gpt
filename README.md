1)git clone https://github.com/arc53/DocsGPT/tree/main#development-environments
2)Добавить а models модель, переименовать ее в docsgpt-7b-f16. Старую модель либо удалить, либо переименовать в любое другое название 
(Например https://huggingface.co/TheBloke/TinyLlama-1.1B-Chat-v0.3-GGUF/blob/main/tinyllama-1.1b-chat-v0.3.Q8_0.gguf)
3)Задать переменные в .env 
LLM_NAME=llama.cpp
VITE_API_STREAMING=true
EMBEDDINGS_NAME=huggingface_sentence-transformers/all-mpnet-base-v2
4)Запус:
	1. Запуcтить все в докер - файл run-with-docker-compose.sh
	2. Запуcтить локальный бэкэнд - файл setup-local-back.sh
	3. Запуcтить локальные фронт и бэк - файл setup-local-back.sh + setup-local-front.sh