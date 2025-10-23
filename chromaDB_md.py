import sys
from enum import auto
from enum import Enum
from pathlib import Path
from typing import Optional
import chromadb
from chromadb.utils import embedding_functions
from chromadb import Collection
from transformers import AutoTokenizer, AutoModel
import os
import re
import time
from docling.document_converter import DocumentConverter
from docling.chunking import HybridChunker
from docling_core.transforms.chunker.tokenizer.huggingface import HuggingFaceTokenizer
import warnings
warnings.filterwarnings("ignore")


#doc = DocumentConverter().convert(source=DOC_SOURCE).document

sentence_transformer_ef = embedding_functions.SentenceTransformerEmbeddingFunction(model_name="all-mpnet-base-v2")


#### Not quite sure yet
EMBED_MODEL_ID = "sentence-transformers/all-mpnet-base-v2"
MAX_TOKENS = 512  # set to a small number for illustrative purposes

tokenizer = HuggingFaceTokenizer(
    tokenizer=AutoTokenizer.from_pretrained(EMBED_MODEL_ID),
    max_tokens=MAX_TOKENS, 
)



class CollectionStatus(Enum):
    COLLECTION_CREATED = auto()
    COLLECTION_EXISTS = auto()


def ensure_collection(client: chromadb.ClientAPI, collection_name: str) -> tuple[str, Optional[Collection]]:
    try:
        # Check if the collection already exists
        collection = client.get_collection(name=collection_name, embedding_function=sentence_transformer_ef)
        print(f"Collection '{collection_name}' already exists.")
        return "COLLECTION_EXISTS", collection
    except Exception:
        # If it doesn't exist, create a new collection
        try:
            collection = client.create_collection(name=collection_name, embedding_function=sentence_transformer_ef)
            print(f"Collection '{collection_name}' created successfully.")
            return "COLLECTION_CREATED", collection
        except Exception as e:
            print(f"Failed to create collection '{collection_name}': {e}")
            return "COLLECTION_CREATION_FAILED", None


def clean_text(raw_text: str) -> str:
    # Clean up the text to remove extra spaces and line breaks
    cleaned_text = raw_text.replace("\n", " ")
    cleaned_text = re.sub(r"\s+", " ", raw_text)
    return cleaned_text



def insert_document(document_path: Path, collection: Collection) -> None:
    """
    Reads a markdown file, splits it into chunks, generates embeddings,
    and inserts the chunks into a ChromaDB collection.
    """
    doc = DocumentConverter().convert(source=str(document_path)).document
    chunker = HybridChunker(
        tokenizer=tokenizer
    )
    chunk_iter = chunker.chunk(dl_doc=doc)
    
    document_chunks = []
    document_ids = []

    document_name = document_path.stem.replace(" ", "-").replace("_", "-")

    for i, chunk in enumerate(chunk_iter):
        #print(chunk)

        document_ids.append(f"{document_name}_chunk{i}")

        enriched_text = chunker.contextualize(chunk=chunk)

        final_chunk = ""
        final_chunk += "Heading: "
        final_chunk += chunk.meta.headings[0]
        final_chunk += " Content: "
        final_chunk += chunk.text

        #print(final_chunk)
        document_chunks.append(final_chunk)
    
    collection.add(
                documents=document_chunks,
                ids=document_ids
            )


## Folder_path = path to e config files
def load_files_into_chroma(folder_path, client: chromadb.ClientAPI, collection_name):
    # Iterate over files in the folder

    collection_status, collection = ensure_collection(client, collection_name)

    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        
        # Only process text files (or adapt as needed for other file types)
        if os.path.isfile(file_path) and file_path.endswith('.txt'):
            # Open and read the content of each file
            with open(file_path, 'r', encoding='utf-8') as f:
                file_content = f.read()
            
            # Add the file content to the Chroma collection as a new chunk
            collection.add(
                documents=[file_content],
                metadatas=[{"filename": filename}],
                ids=[filename]
            )
            print(f"Added {filename} to Chroma database.")



def main() -> None:
    base_directory = Path(os.getcwd())
    db_directory = Path("./db")

    # Prompt user for folder path
    folder_input = input("Enter the path to the folder you want to load into ChromaDB: ").strip()
    files_directory = Path(folder_input)

    # Prompt user for collection name
    collection_name = input("Enter the name of the collection to insert all files into: ").strip()

    # Ensure DB directory exists
    if not db_directory.exists():
        db_directory.mkdir()

    # Check if folder exists
    if not files_directory.exists():
        print(f"The folder '{files_directory}' does not exist! Abort.")
        sys.exit(1)

    # Initialize ChromaDB client
    chroma_client = chromadb.PersistentClient(path=str(db_directory))

    # Ensure or create collection
    collection_status, collection = ensure_collection(chroma_client, collection_name)

    if collection_status == CollectionStatus.COLLECTION_EXISTS:
        print(f"Collection '{collection_name}' already exists. New files will be added to it.")
    else:
        print(f"Created new collection '{collection_name}'.")

    # Loop through all files in the folder
    for file_path in files_directory.iterdir():
        if file_path.is_file() and file_path.suffix.lower() in [".md", ".txt"]:
            print(f"\nProcessing file: {file_path.name}")
            try:
                insert_document(file_path, collection)
                print(f"✅ Inserted '{file_path.name}' into '{collection_name}'")
            except Exception as e:
                print(f"❌ Failed to insert '{file_path.name}': {e}")

    print("\nSetup completed.")

    # Example query for testing
    try:
        result = collection.query(
            query_texts=["What is IBM POWER"],
            n_results=5,
            include=["documents"]
        )
        print("\nExample query results:")
        print(result)
    except Exception as e:
        print(f"Query test failed: {e}")

if __name__ == "__main__":
    main()

