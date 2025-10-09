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
sudo dnf install git bzip2 gcc g++ zlib-devel vim gcc-toolset-12
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
pip install -U --extra-index-url https://repo.fury.io/mgiessing     --prefer-binary chromadb transformers psutil langchain     sentence_transformers gradio==3.50.2 llama-cpp-python scikit-learn     docling einops openai
```

Check installed packages:

```bash
pip list
```

---

## 🗃️ Build the Vector Database

1. Navigate to the project directory:

   ```bash
   cd ~/RAG_public
   rm -rf db
   ```

2. Edit the `database_setup.txt` file to define collections:

   ```bash
   vim database_setup.txt
   ```

   Example configuration:
   ```
   POWER10:IBM P10 Scale Out Servers Technical Overview - redp5675.md
   POWER9:IBM Power System E950 Technical Overview and Introduction - redp5509.md
   ```

3. Populate the database:

   ```bash
   python chromaDB_md.py
   ```

   This process may take up to 5 minutes.

---

## ⚙️ Run the Inference Server

Run **Ollama** (based on `llama.cpp`) as a container:

```bash
podman run -d --name ollama --replace -p 11434:11434 -v ollama:/root/.ollama quay.io/anchinna/ollama:v2
podman exec -it ollama /opt/ollama/ollama pull granite3.3:2b
```

The Granite 3.3 2B model is a **4-bit quantized** model optimized for performance on IBM Power.

---

## 💬 Run the RAG Application

Start the chatbot application:

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
python run_model_openai_backend.py
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

