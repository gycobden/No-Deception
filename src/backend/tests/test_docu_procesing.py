from src.backend.database import pipeline
import pytest
from reportlab.pdfgen import canvas
import os

@pytest.fixture
def sample_pdf(tmp_path):
    pdf_path = tmp_path / "test_doc.pdf"
    c = canvas.Canvas(str(pdf_path))
    c.drawString(100, 750, "Title: Testing PDF Generation")
    c.drawString(100, 730, "Author: John Doe")
    c.drawString(100, 710, "This is a test document used for unit testing.")
    c.save()
    return pdf_path

def test_pdf_processing_pipeline(sample_pdf):
    # Your document processing function should accept a path
    processed, document = pipeline.process_file(str(sample_pdf))
    
    assert isinstance(processed, list)  # or whatever structure you expect
    assert isinstance(document, str)
    sample_processed = processed[0]
    assert "source_author" in sample_processed
    assert "source_title" in sample_processed
    assert "text_chunk" in sample_processed
    assert "id" in sample_processed
    assert "embedding" in sample_processed
