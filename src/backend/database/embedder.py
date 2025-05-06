from sentence_transformers import SentenceTransformer

"""
Embed the given text chunks using HuggingFaces' embedding model and returns
the list of embedding to the client

Args:
    chunks: The list of text chunks, supplied by the client
    model: the embedding model to be used. Defaults to all-MiniLM-L6-v2
    convert_to_numpy: Whether to convert the result to list of numpy arrays.
                        default to true.

Returns:
    embeddings: The list of embeddings that can be supplied to vector database clients
"""

def embed_chunk(chunks, model="all-MiniLM-L6-v2", convert_to_numpy=True):
    embedding_model = SentenceTransformer(model)
    embeddings = embedding_model.encode(chunks, convert_to_numpy=convert_to_numpy)
    return embeddings 

