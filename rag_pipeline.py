"""
RAG pipeline for the workshop.

This module keeps the logic separate from the notebook UI and Streamlit app.
Each function maps to one step in the RAG flow so it is easy to explain live.
"""

from __future__ import annotations

import os
import re
import shutil
from pathlib import Path
from typing import Iterable

from dotenv import load_dotenv
from langchain_community.document_loaders import PyMuPDFLoader, TextLoader
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma
from langchain_core.documents import Document
from langchain_core.language_models.chat_models import BaseChatModel
from langchain_core.prompts import ChatPromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_ollama import ChatOllama
from langchain_text_splitters import RecursiveCharacterTextSplitter

load_dotenv()

# Paths relative to this file so the repo works from any working directory.
ROOT_DIR = Path(__file__).resolve().parent
DEFAULT_DOCS_DIR = ROOT_DIR / "sample_docs"
DEFAULT_CHROMA_DIR = ROOT_DIR / "chroma_db"
DEFAULT_COLLECTION = "workshop_docs"

# Small, fast embedding model that runs locally after first download.
LOCAL_EMBEDDING_MODEL = "sentence-transformers/all-MiniLM-L6-v2"
DEFAULT_CHUNK_SIZE = 1000
DEFAULT_CHUNK_OVERLAP = 100
DEFAULT_RETRIEVAL_K = 6

DEFAULT_LLM_PROVIDER = "ollama"
DEFAULT_OLLAMA_MODEL = "llama3.2:1b"
DEFAULT_GEMINI_MODEL = "gemini-2.5-flash"


def get_embeddings() -> HuggingFaceEmbeddings:
    """Return a local embedding model (downloads once, then works offline)."""
    return HuggingFaceEmbeddings(model_name=LOCAL_EMBEDDING_MODEL)


def get_llm_provider() -> str:
    """Return configured LLM provider: ollama or gemini."""
    return os.getenv("LLM_PROVIDER", DEFAULT_LLM_PROVIDER).strip().lower()


def get_llm(model: str | None = None) -> BaseChatModel:
    """Return the chat model for answer generation (Ollama by default)."""
    provider = get_llm_provider()

    if provider == "gemini":
        api_key = os.getenv("GEMINI_API_KEY")
        if not api_key or api_key == "your_key_here":
            raise ValueError(
                "Missing GEMINI_API_KEY. Set LLM_PROVIDER=ollama for free local use, "
                "or add a Gemini key from https://aistudio.google.com/apikey"
            )
        gemini_model = model or os.getenv("GEMINI_MODEL", DEFAULT_GEMINI_MODEL)
        return ChatGoogleGenerativeAI(
            model=gemini_model, google_api_key=api_key, temperature=0.2
        )

    if provider == "ollama":
        ollama_model = model or os.getenv("OLLAMA_MODEL", DEFAULT_OLLAMA_MODEL)
        base_url = os.getenv("OLLAMA_BASE_URL", "http://localhost:11434")
        return ChatOllama(model=ollama_model, base_url=base_url, temperature=0.2)

    raise ValueError(
        f"Unknown LLM_PROVIDER '{provider}'. Use 'ollama' or 'gemini'."
    )


def normalize_pdf_text(text: str) -> str:
    """Light cleanup for text extracted from PDF pages."""
    text = text.replace("\xa0", " ")
    text = re.sub(r"[ \t]+", " ", text)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip()


def load_pdf(path: Path) -> list[Document]:
    """Load a PDF one page per document using PyMuPDF (better than PyPDF)."""
    documents = PyMuPDFLoader(str(path)).load()
    loaded: list[Document] = []
    for doc in documents:
        doc.page_content = normalize_pdf_text(doc.page_content)
        if not doc.page_content:
            continue
        doc.metadata["source"] = path.name
        doc.metadata["file_type"] = "pdf"
        loaded.append(doc)
    return loaded


def _is_pdf_page(doc: Document) -> bool:
    return doc.metadata.get("file_type") == "pdf"


def load_documents(docs_dir: Path | str = DEFAULT_DOCS_DIR) -> list[Document]:
    """Load all .txt and .pdf files from a folder."""
    docs_dir = Path(docs_dir)
    documents: list[Document] = []
    txt_stems = {path.stem for path in docs_dir.glob("*.txt")}

    for path in sorted(docs_dir.glob("**/*")):
        if path.suffix.lower() == ".txt":
            loader = TextLoader(str(path), encoding="utf-8")
            documents.extend(loader.load())
        elif path.suffix.lower() == ".pdf":
            if path.stem in txt_stems:
                continue
            documents.extend(load_pdf(path))

    if not documents:
        raise FileNotFoundError(f"No documents found in {docs_dir}")

    for doc in documents:
        doc.metadata["source"] = Path(doc.metadata.get("source", "unknown")).name

    return documents


def split_documents(
    documents: Iterable[Document],
    chunk_size: int = DEFAULT_CHUNK_SIZE,
    chunk_overlap: int = DEFAULT_CHUNK_OVERLAP,
) -> list[Document]:
    """Split documents into smaller chunks for retrieval."""
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap,
        separators=["\n\n", "\n", ". ", " ", ""],
    )
    docs = list(documents)
    chunks: list[Document] = []
    to_split: list[Document] = []
    max_pdf_page_chars = chunk_size * 2

    for doc in docs:
        if _is_pdf_page(doc) and len(doc.page_content) <= max_pdf_page_chars:
            chunks.append(doc)
        else:
            to_split.append(doc)

    if to_split:
        chunks.extend(splitter.split_documents(to_split))

    return chunks


def build_vector_store(
    chunks: list[Document],
    persist_directory: Path | str = DEFAULT_CHROMA_DIR,
    collection_name: str = DEFAULT_COLLECTION,
) -> Chroma:
    """Embed chunks and store them in a local ChromaDB database."""
    persist_directory = Path(persist_directory)
    if persist_directory.exists():
        shutil.rmtree(persist_directory)
    persist_directory.mkdir(parents=True, exist_ok=True)

    return Chroma.from_documents(
        documents=chunks,
        embedding=get_embeddings(),
        collection_name=collection_name,
        persist_directory=str(persist_directory),
    )


def load_vector_store(
    persist_directory: Path | str = DEFAULT_CHROMA_DIR,
    collection_name: str = DEFAULT_COLLECTION,
) -> Chroma:
    """Load an existing local ChromaDB store."""
    return Chroma(
        collection_name=collection_name,
        embedding_function=get_embeddings(),
        persist_directory=str(persist_directory),
    )


RAG_PROMPT = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "You are a helpful assistant. Answer ONLY using the provided context. "
            "The context may arrive in multiple chunks; combine related chunks when needed. "
            "If the answer is not in the context, say: "
            "'I could not find that in the provided documents.' "
            "Keep answers clear and concise. Mention the source file when helpful.",
        ),
        (
            "human",
            "Context:\n{context}\n\nQuestion: {question}\n\nAnswer:",
        ),
    ]
)


def format_context(documents: list[Document]) -> str:
    """Turn retrieved chunks into one prompt context block."""
    parts: list[str] = []
    for index, doc in enumerate(documents, start=1):
        source = doc.metadata.get("source", "unknown")
        parts.append(f"[Chunk {index} | Source: {source}]\n{doc.page_content}")
    return "\n\n".join(parts)


def retrieve_documents(
    vector_store: Chroma,
    question: str,
    k: int = DEFAULT_RETRIEVAL_K,
) -> list[Document]:
    """Find the most relevant chunks for a question."""
    return vector_store.similarity_search(question, k=k)


def answer_question(
    vector_store: Chroma,
    question: str,
    k: int = DEFAULT_RETRIEVAL_K,
    llm: BaseChatModel | None = None,
) -> dict[str, str | list[str]]:
    """Run the full RAG flow: retrieve, prompt, generate."""
    llm = llm or get_llm()
    retrieved = retrieve_documents(vector_store, question, k=k)
    context = format_context(retrieved)
    messages = RAG_PROMPT.format_messages(context=context, question=question)
    response = llm.invoke(messages)

    return {
        "answer": response.content,
        "sources": [doc.metadata.get("source", "unknown") for doc in retrieved],
        "context": context,
    }


def build_pipeline_from_folder(
    docs_dir: Path | str = DEFAULT_DOCS_DIR,
    persist_directory: Path | str = DEFAULT_CHROMA_DIR,
) -> Chroma:
    """One-call helper: load docs, chunk, embed, and persist locally."""
    documents = load_documents(docs_dir)
    chunks = split_documents(documents)
    return build_vector_store(chunks, persist_directory=persist_directory)
