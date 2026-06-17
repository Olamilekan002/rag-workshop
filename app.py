"""
Local chat interface for the RAG workshop.

Run from the repo root:
    streamlit run app.py
"""

from __future__ import annotations

import streamlit as st

from rag_pipeline import (
    DEFAULT_CHROMA_DIR,
    DEFAULT_DOCS_DIR,
    answer_question,
    build_pipeline_from_folder,
    load_vector_store,
)

st.set_page_config(page_title="RAG Workshop Chat", page_icon="📚", layout="centered")

st.title("Talk to Your Documents")
st.caption("Workshop demo: Retrieval-Augmented Generation running locally on your laptop")

with st.sidebar:
    st.header("Setup")
    st.markdown(
        """
        1. Add your `GEMINI_API_KEY` in `.env`
        2. Build or load the vector store below
        3. Ask questions in the chat
        """
    )

    if st.button("Build vector store from sample docs"):
        with st.spinner("Loading documents, chunking, and embedding..."):
            build_pipeline_from_folder(DEFAULT_DOCS_DIR, DEFAULT_CHROMA_DIR)
        st.success("Vector store ready.")

    if DEFAULT_CHROMA_DIR.exists():
        st.info("Found local vector store at `chroma_db/`")
    else:
        st.warning("No vector store yet. Click the button above first.")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])
        if message.get("sources"):
            st.caption("Sources: " + ", ".join(message["sources"]))

question = st.chat_input("Ask a question about your documents...")

if question:
    st.session_state.messages.append({"role": "user", "content": question})
    with st.chat_message("user"):
        st.markdown(question)

    with st.chat_message("assistant"):
        try:
            if not DEFAULT_CHROMA_DIR.exists():
                raise FileNotFoundError(
                    "Vector store not found. Use the sidebar button to build it first."
                )

            vector_store = load_vector_store(DEFAULT_CHROMA_DIR)
            with st.spinner("Retrieving context and generating answer..."):
                result = answer_question(vector_store, question)

            st.markdown(result["answer"])
            st.caption("Sources: " + ", ".join(result["sources"]))

            st.session_state.messages.append(
                {
                    "role": "assistant",
                    "content": result["answer"],
                    "sources": result["sources"],
                }
            )
        except Exception as exc:
            st.error(str(exc))
