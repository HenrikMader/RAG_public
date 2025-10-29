# RAG Pipeline Demo on IBM Power based on the IBM RedBooks

This repository demonstrates how to set up a **Retrieval-Augmented Generation (RAG)** pipeline on an **IBM Power LPAR** environment.  
It includes environment setup, model integration, and vector database management for AI inference using **IBM Granite models**.

---

## 📦 Key Components

- **Power LPAR** – Target environment for deployment  
- **Micromamba + Python** – Lightweight package and environment management  
- **Gradio** – Web-based UI for chatbot interaction  
- **ChromaDB** – Vector database for document embeddings  
- **HuggingFace Granite (4-bit, GGUF)** – Large Language Model for inference  
- **LangChain + Docling** – Document chunking and RAG integration  
- **Optional:** Ansible – Automation support

---

## 🧰 Prerequisites

Install required system packages:

```bash
sudo dnf install git mesa-libGL bzip2 gcc g++ zlib-devel vim gcc-toolset-12
```

Clone the project repository:

```bash
git clone https://github.com/HenrikMader/RAG_public
cd RAG_public
```

---

## 🐍 Environment Setup

### 1. Install Micromamba

```bash
cd ~
curl -Ls https://micro.mamba.pm/api/micromamba/linux-ppc64le/latest | tar -xvj bin/micromamba
eval "$(micromamba shell hook --shell bash)"
micromamba --version
```

### 2. Create a Python environment

```bash
micromamba create -n rag_env python=3.11
micromamba activate rag_env
```

### 3. Install dependencies

```bash
micromamba install -c rocketce -c defaults pytorch-cpu pyyaml httptools onnxruntime "pandas<1.6.0" tokenizers
```

Then install additional packages via pip:

```bash
pip install -U --extra-index-url https://repo.fury.io/mgiessing     --prefer-binary streamlit chromadb transformers psutil langchain     sentence_transformers gradio==3.50.2 llama-cpp-python scikit-learn     docling einops openai
```

Check installed packages:

```bash
pip list
```

---

## 🗃️  Convert PDF files to Markdown


   With the script 

   ``converted_docling.py```
   
   you can convert a folder which contains pdf files to markdown files.

   ```bash
   python converted_docling.py
   ```

   When prompted with the path for your pdf files, take in the absolute path to a folder which contains all of your PDF files. The output folder for markdown does not need to exist.


---

## 🗃️ Build the Vector Database

1. Navigate to the project directory:

   ```bash
   cd ~/RAG_public
   rm -rf db
   ```


2. Populate the database:

   ```bash
   python chromaDB_md.py
   ```
   Insert the pull path to the converted Markdown files when prompted. 
   Afterwards, you need to insert a name for the collection that you are creating.

   This process may take up several minutes.

---

## ⚙️ Run the Inference Server

Run **Ollama** (based on `llama.cpp`) as a container:

```bash
podman run -d --name ollama --replace -p 11434:11434 -v ollama:/root/.ollama quay.io/anchinna/ollama:v2
podman exec -it ollama /opt/ollama/ollama pull granite3.3:2b
```

Note: If you want to use Granite 4, then run the following container:
```bash
podman run -d --name ollama --replace -p 11434:11434 -v ollama:/root/.ollama quay.io/anchinna/ollama:v3
podman exec -it ollama /opt/ollama/ollama pull granite4:tiny-h
```


---

## 💬 Run the RAG Application

Start the chatbot application:

```bash
streamlit run streamlit_adv.py --server.port 7680
```


Note: Old Gradio Frontend (Does not need to be started if you want to use new frontend (streamlit))
```bash
python run_model_openai_backend.py
```


Access the web UI:

```
http://<IP_of_your_machine>:7680
```

---

## 🧩 Manage the Vector Database

Stop the chatbot (`Ctrl + C`) and start the admin interface:

```bash
python admin_database.py
```

Access the admin UI at:

```
http://<IP_of_your_machine>:8082
```

From here, you can:
- List collections  
- Add or remove Markdown files  
- View chunk statistics per collection  

Example: Add a new document to the Power10 collection:

```bash
./files_for_database/db_files_md/IBM Power E1050 Technical Overview and Introduction - redp5684.md
```

After ingestion, restart the chatbot to query new data.

---

## 🔍 Query the RAG System

Re-launch the chatbot app:

```bash
streamlit run streamlit_adv.py --server.port 7680
```



Then open:

```
http://<IP_of_your_machine>:7680
```

Now you can ask questions about all loaded documents (e.g., Power10, Power9, E1050).

---

## 🔗 Additional Resources

- [Sizing AI workloads on IBM Power](https://community.ibm.com/community/user/blogs/sebastian-lehrig/2024/03/26/sizing-for-ai)  
- [Running vLLM on PPC64LE architecture](https://community.ibm.com/community/user/blogs/manjunath-kumatagi/2024/06/27/run-vllm-on-ppc64le-architecture)

---

