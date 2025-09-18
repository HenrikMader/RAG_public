import gradio as gr
import chromadb
from chromadb.utils import embedding_functions
from chromadb import Collection

from docling.document_converter import DocumentConverter
from docling.chunking import HybridChunker
from docling_core.transforms.chunker.tokenizer.huggingface import HuggingFaceTokenizer
from transformers import AutoTokenizer

from pathlib import Path
import re

# --- Setup ChromaDB client ---
chroma_client = chromadb.PersistentClient(path="./db")
embedding_fn = embedding_functions.SentenceTransformerEmbeddingFunction(model_name="all-mpnet-base-v2")

EMBED_MODEL_ID = "sentence-transformers/all-mpnet-base-v2"
MAX_TOKENS = 512

tokenizer = HuggingFaceTokenizer(
    tokenizer=AutoTokenizer.from_pretrained(EMBED_MODEL_ID),
    max_tokens=MAX_TOKENS,
)

# --- Core Utility Functions ---

def ensure_collection(client: chromadb.ClientAPI, collection_name: str) -> Collection:
    try:
        return client.get_collection(name=collection_name, embedding_function=embedding_fn)
    except Exception:
        return client.create_collection(name=collection_name, embedding_function=embedding_fn)

def insert_markdown_to_collection(md_file, collection_name):
    try:
        # Ensure collection exists
        collection = ensure_collection(chroma_client, collection_name)

        file_path = Path(md_file.name)
        document_name = file_path.stem.replace(" ", "-").replace("_", "-")

        doc = DocumentConverter().convert(source=md_file.name).document
        chunker = HybridChunker(tokenizer=tokenizer)
        chunk_iter = chunker.chunk(dl_doc=doc)

        document_chunks = []
        document_ids = []

        for i, chunk in enumerate(chunk_iter):
            doc_id = f"{document_name}_chunk{i}"
            chunk_text = f"Heading: {chunk.meta.headings[0]} Content: {chunk.text}"
            document_ids.append(doc_id)
            document_chunks.append(chunk_text)

        collection.add(documents=document_chunks, ids=document_ids)

        return f"✅ Successfully added {len(document_ids)} chunks to collection '{collection_name}'"
    except Exception as e:
        return f"❌ Failed to insert document: {e}"

def insert_markdown_from_path(path_str, collection_name):
    try:
        collection = ensure_collection(chroma_client, collection_name)

        path = Path(path_str)
        if not path.exists():
            return f"❌ Path '{path}' does not exist."

        files_to_process = []
        if path.is_file() and path.suffix == ".md":
            files_to_process = [path]
        elif path.is_dir():
            files_to_process = [p for p in path.glob("*.md")]
        else:
            return f"❌ Invalid file or folder: {path}"

        if not files_to_process:
            return "⚠️ No markdown (.md) files found."

        total_chunks = 0
        total_files = len(files_to_process)
        for idx, file_path in enumerate(files_to_process, start=1):
            print(f"Processing file {idx} of {total_files}: {file_path.name}")  # progress bar on terminal
            
            doc = DocumentConverter().convert(source=str(file_path)).document
            chunker = HybridChunker(tokenizer=tokenizer)
            chunk_iter = chunker.chunk(dl_doc=doc)

            document_chunks = []
            document_ids = []

            document_name = file_path.stem.replace(" ", "-").replace("_", "-")
            for i, chunk in enumerate(chunk_iter):
                doc_id = f"{document_name}_chunk{i}"
                chunk_text = f"Heading: {chunk.meta.headings[0]} Content: {chunk.text}"
                document_ids.append(doc_id)
                document_chunks.append(chunk_text)

            collection.add(documents=document_chunks, ids=document_ids)
            total_chunks += len(document_ids)

        return f"✅ Imported {total_files} file(s) with total {total_chunks} chunks into '{collection_name}'"
    except Exception as e:
        return f"❌ Failed to insert documents: {e}"

def list_collections():
    try:
        collections = chroma_client.list_collections()
        return [col.names for col in collections]
    except Exception as e:
        return [f"Error: {e}"]

def delete_collection(collection_name):
    try:
        chroma_client.delete_collection(name=collection_name)
        return f"✅ Deleted collection '{collection_name}'"
    except Exception as e:
        return f"❌ Failed to delete collection '{collection_name}': {e}"

def list_documents(collection_name):
    try:
        collection = chroma_client.get_collection(name=collection_name, embedding_function=embedding_fn)
        results = collection.get()
        ids = results["ids"]

        if not ids:
            return "No documents found in this collection."

        # Create a mapping filename -> list of chunks
        file_to_chunks = {}
        for doc_id in ids:
            # Extract filename prefix before '_chunk'
            m = re.match(r"(.+)_chunk\d+", doc_id)
            filename = m.group(1) if m else "UnknownFile"
            file_to_chunks.setdefault(filename, []).append(doc_id)

        # Format output nicely
        output_lines = []
        for filename, chunks in file_to_chunks.items():
            output_lines.append(f"File: {filename} ({len(chunks)} chunks)")
            #for chunk_id in chunks:
            #    output_lines.append(f"  - {chunk_id}")
            #output_lines.append("")  # blank line for separation

        return "\n".join(output_lines)
    except Exception as e:
        return f"Error: {e}"

def delete_document(collection_name, document_id):
    try:
        collection = chroma_client.get_collection(name=collection_name, embedding_function=embedding_fn)
        collection.delete(ids=[document_id])
        return f"✅ Deleted document ID '{document_id}' from '{collection_name}'"
    except Exception as e:
        return f"❌ Failed to delete document: {e}"

# --- Gradio Interface ---
with gr.Blocks(title="ChromaDB Admin UI") as demo:
    gr.Markdown("## 🧠 ChromaDB Vector Database Admin Panel")

    with gr.Row():
        collection_output = gr.Textbox(label="Collections", lines=5)
    with gr.Row():
        collection_list_btn = gr.Button("🔄 List Collections")

    with gr.Row():
        del_col_name = gr.Textbox(label="Collection to Delete")
    with gr.Row():
        del_col_output = gr.Textbox(label="Delete Status")
    with gr.Row():
        del_col_btn = gr.Button("❌ Delete Collection")

    with gr.Row():
        doc_col_name = gr.Textbox(label="Collection Name (to list docs)")
    with gr.Row():
        doc_ids_output = gr.Textbox(label="Document IDs", lines=15)
    with gr.Row():
        list_docs_btn = gr.Button("📄 List Documents")

    with gr.Row():
        del_doc_col = gr.Textbox(label="Collection Name")
    with gr.Row():
        del_doc_id = gr.Textbox(label="Document ID to Delete")
    with gr.Row():
        del_doc_output = gr.Textbox(label="Document Delete Status")
    with gr.Row():
        del_doc_btn = gr.Button("🗑️  Delete Document")

    gr.Markdown("---")

    with gr.Row():
        upload_collection_name = gr.Textbox(label="Target Collection Name for Upload")
    with gr.Row():
        md_file_upload = gr.File(label="Upload Markdown (.md) File", file_types=[".md"])
    with gr.Row():
        upload_output = gr.Textbox(label="Upload Status")
    with gr.Row():
        upload_btn = gr.Button("📤 Upload Markdown to Collection")

    gr.Markdown("### 📂 Import Markdown Files from Local Path")

    with gr.Row():
        local_path_input = gr.Textbox(label="Path to File or Folder (must be .md)", placeholder="./my_docs")
    with gr.Row():
        local_path_collection = gr.Textbox(label="Target Collection Name")
    with gr.Row():
        local_path_output = gr.Textbox(label="Import Status")
    with gr.Row():
        local_path_btn = gr.Button("📁 Import from Path")

    local_path_btn.click(
        fn=insert_markdown_from_path,
        inputs=[local_path_input, local_path_collection],
        outputs=local_path_output,
    )

    # --- Button Functionality Bindings ---
    collection_list_btn.click(fn=list_collections, outputs=collection_output)
    del_col_btn.click(fn=delete_collection, inputs=del_col_name, outputs=del_col_output)
    list_docs_btn.click(fn=list_documents, inputs=doc_col_name, outputs=doc_ids_output)
    del_doc_btn.click(fn=delete_document, inputs=[del_doc_col, del_doc_id], outputs=del_doc_output)
    upload_btn.click(fn=insert_markdown_to_collection, inputs=[md_file_upload, upload_collection_name], outputs=upload_output)

# --- Launch App ---
demo.launch(server_name="0.0.0.0", server_port=8082)

