import pytest
from src.backend.database.chroma_client import MetadataDict, ChromaClient
import tempfile

@pytest.fixture
def test_metadata():
    return MetadataDict(
        id="test123",
        embedding=[0.1, 0.2, 0.3],
        text_chunk="This is a test chunk of text.",
        source_title="Test Title",
        source_author="Test Author"
    )

@pytest.fixture
def test_document():
    return "This is the full document string."

@pytest.fixture
def test_client():
    tempdir = tempfile.mkdtemp()
    
    return ChromaClient({'db_dir': tempdir}, collection_name="dummy_collection", remote=False)


def test_metadata_to_dict(test_metadata):
    result = test_metadata.to_dict()
    assert result["id"] == "test123"
    assert result["embedding"] == [0.1, 0.2, 0.3]
    assert result["text_chunk"] == "This is a test chunk of text."
    assert result["source_title"] == "Test Title"
    assert result["source_author"] == "Test Author"

def test_add_and_get_document(test_metadata, test_document, test_client):
    document = test_client.add_document(test_document, [test_metadata.to_dict()])
    assert document == test_document

    result = test_client.get_document_by_id(test_metadata.id)
    assert result["ids"][0] == test_metadata.id
    assert result["documents"][0] == test_metadata.text_chunk
    assert result["metadatas"][0]["source_title"] == test_metadata.source_title
    assert result["metadatas"][0]["source_author"] == test_metadata.source_author
    
def test_find_similar_documents(test_metadata, test_document, test_client):
    # Ensure the document is in the DB
    document = test_client.add_document(test_document, [test_metadata.to_dict()])
    assert document == test_document

    results = test_client.find_similar_documents(test_metadata.embedding, n_results=1)
    assert results["documents"][0][0] == test_metadata.text_chunk
    assert results["metadatas"][0][0]["source_title"] == test_metadata.source_title
    assert results["metadatas"][0][0]["source_author"] == test_metadata.source_author
    assert results["ids"][0][0] == test_metadata.id

