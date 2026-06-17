#!/usr/bin/env python3
"""Build the local ChromaDB store before the workshop (optional fallback)."""

from rag_pipeline import DEFAULT_CHROMA_DIR, DEFAULT_DOCS_DIR, build_pipeline_from_folder


def main() -> None:
    print("Building local vector store...")
    print(f"Documents: {DEFAULT_DOCS_DIR}")
    print(f"Output:    {DEFAULT_CHROMA_DIR}")
    build_pipeline_from_folder(DEFAULT_DOCS_DIR, DEFAULT_CHROMA_DIR)
    print("Done. You can now run: streamlit run app.py")


if __name__ == "__main__":
    main()
