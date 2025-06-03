import os

# Get the absolute path to the project root (adjust as needed)
PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))

# Define absolute path to ChromaDB store
CHROMA_PATH = os.path.abspath(os.path.join(PROJECT_ROOT, "src/backend/database/chroma_store"))

COLLECTION_NAME = "vaccines"
DATA_FOLDER = os.path.abspath(os.path.join(PROJECT_ROOT, "src/backend/articles"))
REMOTE_ADDRESS = "localhost"
REMOTE_PORT = 8000

REMOTE_ACCESS = False