import os
import sys
import argparse
import shutil
from src.backend.database.chroma_client import ChromaClient
from src.backend.database.pipeline import process_folder

# Choose a consistent path for persistent ChromaDB
CHROMA_PATH = "src/backend/database/chroma_store"
COLLECTION_NAME = "vaccines"

def str2bool(value):
    return value.lower() in ("true")

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--reset", type=str2bool, nargs='?', const=True, default=False, help="Reset and reinitialize ChromaDB")
    args = parser.parse_args()
    print(args.reset)

    if args.reset:
        if os.path.exists(CHROMA_PATH):
            print(f"🔄 Resetting ChromaDB at {CHROMA_PATH}...")
            shutil.rmtree(CHROMA_PATH)
            print("✅ ChromaDB directory deleted.")
        else:
            print("ℹ️ ChromaDB path does not exist, nothing to delete.")

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
