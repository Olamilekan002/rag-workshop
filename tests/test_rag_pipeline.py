"""Workshop tests for document loading, chunking, and pipeline helpers."""

from __future__ import annotations

import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from rag_pipeline import (  # noqa: E402
    DEFAULT_DOCS_DIR,
    format_context,
    load_documents,
    load_pdf,
    split_documents,
)


def test_sample_docs_exist() -> None:
    assert DEFAULT_DOCS_DIR.exists()
    files = list(DEFAULT_DOCS_DIR.glob("*.txt"))
    assert len(files) >= 3


def test_load_documents_returns_content() -> None:
    documents = load_documents(DEFAULT_DOCS_DIR)
    assert len(documents) >= 3
    assert all(doc.page_content.strip() for doc in documents)
    assert all("source" in doc.metadata for doc in documents)


def test_split_documents_creates_multiple_chunks() -> None:
    documents = load_documents(DEFAULT_DOCS_DIR)
    chunks = split_documents(documents, chunk_size=200, chunk_overlap=20)
    assert len(chunks) > len(documents)
    assert all(chunk.page_content.strip() for chunk in chunks)


def test_format_context_includes_sources() -> None:
    documents = load_documents(DEFAULT_DOCS_DIR)
    chunks = split_documents(documents[:1], chunk_size=200, chunk_overlap=20)
    context = format_context(chunks[:2])
    assert "Source:" in context
    assert "Chunk 1" in context
    assert "Chunk 2" in context


def test_ifs415_erp_section_stays_in_one_chunk() -> None:
    pdf_path = DEFAULT_DOCS_DIR / "ifs415_lecture_notes.pdf"
    if not pdf_path.exists():
        pytest.skip("IFS 415 lecture notes PDF not found")

    documents = load_pdf(pdf_path)
    chunks = split_documents(documents)
    erp_chunks = [
        chunk
        for chunk in chunks
        if chunk.metadata.get("source") == pdf_path.name
        and "erp architecture" in chunk.page_content.lower()
    ]
    assert erp_chunks
    assert any(
        "flexible architecture" in chunk.page_content.lower()
        and "implementation team" in chunk.page_content.lower()
        for chunk in erp_chunks
    )
