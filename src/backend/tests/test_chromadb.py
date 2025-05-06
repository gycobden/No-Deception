import pytest, pprint
from database.chroma_client import MetadataDict, add_document, get_document_by_id, find_similar_documents

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

def test_metadata_to_dict(test_metadata):
    result = test_metadata.to_dict()
    assert result["id"] == "test123"
    assert result["embedding"] == [0.1, 0.2, 0.3]
    assert result["text_chunk"] == "This is a test chunk of text."
    assert result["source_title"] == "Test Title"
    assert result["source_author"] == "Test Author"

def test_add_and_get_document(test_metadata, test_document):
    doc_id = add_document(test_document, test_metadata.to_dict())
    assert doc_id == test_metadata.id

    result = get_document_by_id(doc_id)
    assert result["ids"][0] == test_metadata.id
    assert result["documents"][0] == test_document
    assert result["metadatas"][0]["source_title"] == test_metadata.source_title
    assert result["metadatas"][0]["source_author"] == test_metadata.source_author
    assert result["metadatas"][0]["text_chunk"] == test_metadata.text_chunk
    
def test_find_similar_documents(test_metadata, test_document):
    # Ensure the document is in the DB
    id = add_document(test_document, test_metadata.to_dict())

    results = find_similar_documents(test_metadata.embedding, n_results=1)
    assert "documents" in results
    assert len(results["documents"][0]) >= 1
    assert id == test_metadata.id
    assert results["metadatas"][0][0]["source_title"] == test_metadata.source_title
    assert results["metadatas"][0][0]["source_author"] == test_metadata.source_author
    assert results["metadatas"][0][0]["text_chunk"] == test_metadata.text_chunk
    assert results["metadatas"][0][0]["id"] == test_metadata.id

if __name__ == "__main__":
    # run tests
    
    pytest.main([__file__])