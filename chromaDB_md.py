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
from langchain.text_splitter import MarkdownHeaderTextSplitter, RecursiveCharacterTextSplitter
import time
from docling.document_converter import DocumentConverter
from docling.chunking import HybridChunker
from docling_core.transforms.chunker.tokenizer.huggingface import HuggingFaceTokenizer



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
        print(chunk)

        document_ids.append(f"{document_name}_chunk{i}")

        enriched_text = chunker.contextualize(chunk=chunk)

        final_chunk = ""
        final_chunk += "Heading: "
        final_chunk += chunk.meta.headings[0]
        final_chunk += " Content: "
        final_chunk += chunk.text

        print(final_chunk)
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
    files_directory = Path("./db_files_md")  # Folder containing markdown files

    if not db_directory.exists():
        db_directory.mkdir()

    if not files_directory.exists():
        print("DB files were not copied! Abort.")
        sys.exit(1)

    chroma_client = chromadb.PersistentClient(path=str(db_directory))


    file = open("database_setup.txt")
    for i in file:
        print(i)
        x = i.split(":", 1)
        collection_name = str(x[0]).strip()
        file_name = str(x[1]).strip()
        print("Adding")
        print(file_name)
        print("to")
        print(collection_name)
        
        print(type(collection_name))
        # Ensure the collection exists or create it
        collection_status, collection = ensure_collection(chroma_client, str(collection_name))

        if collection_status == CollectionStatus.COLLECTION_EXISTS:
            print(f"Collection '{collection_name}' already exists. Skipping file insertion.")
        else:
            print(f"Creating collection '{collection_name}' and inserting documents.")
            
            # Process the file
            #document_path = Path(".") / files_directory / Path(file_name)
            document_path = files_directory / file_name
            print(document_path)
            if document_path.exists():
                insert_document(document_path, collection)
                print(f"Inserted {file_name} into {collection_name}")
            else:
                print(f"File {file_name} not found!")
            
    print("Setup completed.")

    # Example query for testing
    result = collection.query(
        query_texts=["What is IBM POWER"],
        n_results=5,
        include=["documents"]
    )
    print(result)


if __name__ == "__main__":
    main()
                                                       
