# python init_chroma.py --reset=True

import sys; sys.dont_write_bytecode = True # prevent creation __pycache__ folder
import os
import argparse
import shutil
import config
from src.backend.database.chroma_client import ChromaClient
from src.backend.database.pipeline import process_folder

def str2bool(value):
    return value.lower() in ("true")

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--reset", type=str2bool, nargs='?', const=True, default=False, help="Reset and reinitialize ChromaDB")
    args = parser.parse_args()
    print(args.reset)

    if args.reset:
        if os.path.exists(config.CHROMA_PATH):
            print(f"🔄 Resetting ChromaDB at {config.CHROMA_PATH}...")
            shutil.rmtree(config.CHROMA_PATH)
            print("✅ ChromaDB directory deleted.")
        else:
            print("ℹ️ ChromaDB path does not exist, nothing to delete.")

    # Check if the ChromaDB path exists (rough indicator of initialization)
    if not os.path.exists(config.CHROMA_PATH) or not os.listdir(config.CHROMA_PATH):
        print("🔧 ChromaDB not found, initializing...")
        client = ChromaClient(db_dir=config.CHROMA_PATH, collection_name=config.COLLECTION_NAME)
        
        # Process articles and add to collection
        process_folder(client, folder_path=config.DATA_FOLDER)
        print("✅ ChromaDB setup complete.")
    else:
        print("✅ ChromaDB already initialized. Skipping setup.")

if __name__ == "__main__":
    main()
