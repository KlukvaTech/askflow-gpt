#!/bin/bash
docker-compose -f docker-compose-local.yaml build && docker-compose -f docker-compose-local.yaml up -d
pip install -r application/requirements.txt
pip install llama-cpp-python
pip install sentence-transformers


export LLM_NAME=llama.cpp
export EMBEDDINGS_NAME=huggingface_sentence-transformers/all-mpnet-base-v2
export FLASK_APP=application/app.py
export FLASK_DEBUG=true
export CELERY_BROKER_URL=redis://localhost:6379/0
export CELERY_RESULT_BACKEND=redis://localhost:6379/1
flask run --host=0.0.0.0 --port=7091 &
celery -A application.app.celery worker -l INFO