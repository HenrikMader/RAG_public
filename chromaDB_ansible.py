import os
from pathlib import Path
import re
import chromadb
from chromadb.utils import embedding_functions
from chromadb import Collection
from transformers import AutoTokenizer
from docling.document_converter import DocumentConverter
from docling.chunking import HybridChunker
from docling_core.transforms.chunker.tokenizer.huggingface import HuggingFaceTokenizer
from enum import auto, Enum

# ---------------- CONFIG ----------------
MARKDOWN_FOLDER = Path("./downloaded_pages_md")  # folder with markdown files
CHROMA_DB_DIR = Path("./chroma_db")             # folder to persist ChromaDB
COLLECTION_NAME = "markdown_docs"

EMBED_MODEL_ID = "sentence-transformers/all-mpnet-base-v2"
MAX_TOKENS = 512

# ---------------- UTILS ----------------
class CollectionStatus(Enum):
    COLLECTION_CREATED = auto()
    COLLECTION_EXISTS = auto()


def clean_text(raw_text: str) -> str:
    """Clean text from excessive spaces and newlines."""
    cleaned = raw_text.replace("\n", " ")
    cleaned = re.sub(r"\s+", " ", cleaned)
    return cleaned


# ---------------- EMBEDDINGS ----------------
# Use SentenceTransformer embeddings
sentence_transformer_ef = embedding_functions.SentenceTransformerEmbeddingFunction(
    model_name=EMBED_MODEL_ID
)

# HuggingFace tokenizer for chunking
tokenizer = HuggingFaceTokenizer(
    tokenizer=AutoTokenizer.from_pretrained(EMBED_MODEL_ID),
    max_tokens=MAX_TOKENS
)

# ---------------- CHROMA SETUP ----------------
def ensure_collection(client: chromadb.ClientAPI, collection_name: str) -> tuple[str, Collection]:
    """Ensure the Chroma collection exists; create if not."""
    try:
        collection = client.get_collection(name=collection_name, embedding_function=sentence_transformer_ef)
        print(f"Collection '{collection_name}' already exists.")
        return "COLLECTION_EXISTS", collection
    except Exception:
        collection = client.create_collection(name=collection_name, embedding_function=sentence_transformer_ef)
        print(f"Collection '{collection_name}' created successfully.")
        return "COLLECTION_CREATED", collection


# ---------------- DOCUMENT INSERTION ----------------
def insert_document(document_path: Path, collection: Collection):
    """
    Read a markdown file, chunk it, embed each chunk, and insert into ChromaDB.
    """
    print("reading")
    print(document_path)
    doc = DocumentConverter().convert(source=str(document_path)).document
    chunker = HybridChunker(tokenizer=tokenizer)
    chunk_iter = chunker.chunk(dl_doc=doc)

    document_chunks = []
    document_ids = []

    document_name = document_path.stem.replace(" ", "-").replace("_", "-")

    for i, chunk in enumerate(chunk_iter):
        chunk_id = f"{document_name}_chunk{i}"
        document_ids.append(chunk_id)

        # Build enriched chunk with heading context
        #final_chunk = ""
        #if chunk.meta.headings:
        #    final_chunk += "Heading: " + " | ".join(chunk.meta.headings) + " "
        #final_chunk += "Content: " + chunk.text
        print("----------------")
        print("Chunk")

        print(chunk.text)
        document_chunks.append(chunk.text)

    # Add to Chroma collection
    collection.add(
        documents=document_chunks,
        ids=document_ids,
        metadatas=[{"source": str(document_path)}] * len(document_chunks)
    )
    print(f"Inserted {len(document_chunks)} chunks from '{document_path.name}'.")


# ---------------- LOAD ALL FILES ----------------
def load_markdown_folder_into_chroma(folder_path: Path, client: chromadb.ClientAPI, collection_name: str):
    collection_status, collection = ensure_collection(client, collection_name)

    for dirpath, _, filenames in os.walk(folder_path):
        for filename in filenames:
            if filename.endswith(".md"):
                file_path = Path(dirpath) / filename
                insert_document(file_path, collection)


# ---------------- MAIN ----------------
def main():
    CHROMA_DB_DIR.mkdir(exist_ok=True)
    chroma_client = chromadb.PersistentClient(path=str(CHROMA_DB_DIR))

    load_markdown_folder_into_chroma(MARKDOWN_FOLDER, chroma_client, COLLECTION_NAME)

    print("✅ All markdown files loaded into ChromaDB.")


if __name__ == "__main__":
    main()

