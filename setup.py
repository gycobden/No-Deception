import os
import chromadb
from src.backend.database.chroma_client import ChromaClient
from src.backend.database.pipeline import process_folder

# Choose a consistent path for persistent ChromaDB
CHROMA_PATH = "src/backend/database/chroma_store"
COLLECTION_NAME = "vaccines"

def main():
    # Check if the ChromaDB path exists (rough indicator of initialization)
    if not os.path.exists(CHROMA_PATH) or not os.listdir(CHROMA_PATH):
        print("🔧 ChromaDB not found, initializing...")
        client = ChromaClient(db_dir=CHROMA_PATH, collection_name=COLLECTION_NAME)
        
        # Process articles and add to collection
        process_folder(client, folder_path="src/backend/articles")
        print("✅ ChromaDB setup complete.")
    else:
        print("✅ ChromaDB already initialized. Skipping setup.")

if __name__ == "__main__":
    main()
