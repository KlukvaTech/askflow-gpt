# Askflow-gpt

## Installation

1. `git clone https://github.com/KlukvaTech/askflow-gpt.git`

2. `huggingface-cli download TheBloke/openchat-3.5-0106-GGUF openchat-3.5-0106.Q4_K_M.gguf —local-dir . —local-dir-use-symlinks False`

2. Переместить вашу модель в папку `models`.

3. Задать переменные в .env

```
LLM_NAME=llama.cpp
VITE_API_STREAMING=false
EMBEDDINGS_NAME=huggingface_sentence-transformers/all-mpnet-base-v2
```

## Usage

1. Запуcтить всё в докере - файл `run-with-docker-compose.sh`
2. Запуcтить локальный бэкэнд - файл `setup-local-back.sh`
3. Запуcтить локальные фронт и бэк - файл `setup-local-back.sh + setup-local-front.sh`