import sys
import os
import re
import time
from pathlib import Path
from enum import Enum, auto
import hashlib
import chromadb
from chromadb.utils import embedding_functions
from chromadb import Collection
from transformers import AutoTokenizer
from docling.document_converter import DocumentConverter
from docling.chunking import HybridChunker
from docling_core.transforms.chunker.tokenizer.huggingface import HuggingFaceTokenizer

# --- Embedding setup ---
EMBED_MODEL_ID = "sentence-transformers/all-mpnet-base-v2"
MAX_TOKENS = 512
sentence_transformer_ef = embedding_functions.SentenceTransformerEmbeddingFunction(model_name=EMBED_MODEL_ID)

tokenizer = HuggingFaceTokenizer(
    tokenizer=AutoTokenizer.from_pretrained(EMBED_MODEL_ID),
    max_tokens=MAX_TOKENS,
)

# --- Utility Functions ---
class CollectionStatus(Enum):
    COLLECTION_CREATED = auto()
    COLLECTION_EXISTS = auto()

def ensure_collection(client: chromadb.ClientAPI, collection_name: str) -> tuple[str, Collection]:
    """Ensure a collection exists; create it if not."""
    try:
        collection = client.get_collection(name=collection_name, embedding_function=sentence_transformer_ef)
        return "COLLECTION_EXISTS", collection
    except Exception:
        collection = client.create_collection(name=collection_name, embedding_function=sentence_transformer_ef)
        return "COLLECTION_CREATED", collection

def file_id(filepath: Path) -> str:
    """Generate a unique hash ID for a file path."""
    return hashlib.md5(str(filepath).encode("utf-8")).hexdigest()

def insert_document(document_path: Path, collection: Collection) -> None:
    """Chunk, embed, and insert a document into the collection with metadata."""
    doc = DocumentConverter().convert(source=str(document_path)).document
    chunker = HybridChunker(tokenizer=tokenizer)
    chunk_iter = chunker.chunk(dl_doc=doc)

    document_chunks = []
    document_ids = []
    fid = file_id(document_path)

    for i, chunk in enumerate(chunk_iter):
        chunk_text = f"Heading: {chunk.meta.headings[0] if chunk.meta.headings else ''} Content: {chunk.text}"
        document_chunks.append(chunk_text)
        document_ids.append(f"{fid}_{i}")

    # Metadata for all chunks
    metadatas = [
        {
            "file_id": fid,
            "source": str(document_path),
            "last_modified": os.path.getmtime(document_path),
            "filename": document_path.stem
        }
        for _ in document_chunks
    ]

    # Remove old entries (if re-indexing)
    collection.delete(where={"file_id": fid})

    # Insert new chunks
    collection.add(
        documents=document_chunks,
        ids=document_ids,
        metadatas=metadatas
    )
    print(f"✅ Indexed '{document_path}' with {len(document_chunks)} chunks into '{collection.name}'.")

def sync_folder(main_folder: Path, chroma_client: chromadb.ClientAPI):
    """
    Traverse subfolders in main_folder.
    Each subfolder becomes a collection; each .md file is indexed into that collection.
    """
    # Step 1: list all subfolders
    subfolders = [f for f in main_folder.iterdir() if f.is_dir()]

    for folder in subfolders:
        collection_name = folder.name.replace(" ", "-").lower()
        status, collection = ensure_collection(chroma_client, collection_name)

        # List all markdown files in this subfolder
        current_files = {f for f in folder.glob("*.md")}
        current_ids = {file_id(f) for f in current_files}

        # Get files currently in DB
        db_entries = collection.get(include=["metadatas"])
        db_metadatas = db_entries.get("metadatas", [])
        db_ids = {meta["file_id"] for meta in db_metadatas if "file_id" in meta}

        # Add/update files
        for f in current_files:
            fid = file_id(f)
            mtime = os.path.getmtime(f)

            in_db = any(meta for meta in db_metadatas if meta.get("file_id") == fid)
            if not in_db:
                print(f"📥 New file: {f}, indexing...")
                insert_document(f, collection)
            else:
                db_meta = next(meta for meta in db_metadatas if meta.get("file_id") == fid)
                if mtime > db_meta.get("last_modified", 0):
                    print(f"🔄 Updated file: {f}, re-indexing...")
                    insert_document(f, collection)

        # Delete missing files
        for fid in db_ids:
            if fid not in current_ids:
                print(f"🗑️ Removing file with id {fid} (missing in folder).")
                collection.delete(where={"file_id": fid})

def main():
    main_directory = Path("./main")  # top-level folder with subfolders
    db_directory = Path("./db")

    if not db_directory.exists():
        db_directory.mkdir()

    if not main_directory.exists():
        print(f"Folder '{main_directory}' not found! Abort.")
        sys.exit(1)

    chroma_client = chromadb.PersistentClient(path=str(db_directory))

    print("🚀 Starting watcher loop...")
    while True:
        sync_folder(main_directory, chroma_client)
        time.sleep(15)  # check every 15 seconds

if __name__ == "__main__":
    main()
