FROM quay.io/fedora/python-39


RUN pip3 install --prefer-binary --extra-index-url https://repo.fury.io/mgiessing chromadb transformers psutil langchain sentence_transformers gradio==3.50.2 llama-cpp-python

RUN mkdir rag_demo

WORKDIR /rag_demo

COPY db_files_md db_files_md
COPY chromaDB_md.py .
COPY run_model.py .
COPY theme.py .

RUN wget https://huggingface.co/bartowski/granite-3.1-8b-instruct-GGUF/resolve/main/granite-3.1-8b-instruct-Q4_K_M.gguf

RUN python chromaDB_md.py

CMD python run_model.py


