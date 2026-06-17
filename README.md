# Build Your Own RAG System — Workshop Materials

Hands-on materials for the **Build Your Own RAG System from Scratch** workshop.

By the end, you will have a working Retrieval-Augmented Generation (RAG) system that answers questions from documents — running locally on your laptop.

## What's included

```
├── README.md
├── requirements.txt
├── .env.example
├── rag_pipeline.py          # Core RAG logic
├── app.py                   # Local Streamlit chat app
├── scripts/
│   └── build_vector_store.py
├── notebooks/
│   └── 01_rag_workshop.ipynb
├── sample_docs/             # Starter documents
└── docs/
    ├── SETUP_GUIDE.md       # Read this before the event
    └── LOCAL_RUN.md         # How to run everything locally
```

## Quick start

```bash
git clone https://github.com/Olamilekan-Turing/rag-workshop.git
cd rag-workshop

python3 -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate

pip install -r requirements.txt
cp .env.example .env        # add your GEMINI_API_KEY

python scripts/build_vector_store.py
jupyter notebook notebooks/01_rag_workshop.ipynb
streamlit run app.py
```

Get a free Gemini API key: https://aistudio.google.com/apikey

## Before the workshop

Read `docs/SETUP_GUIDE.md` and complete setup **before** you arrive.

## Workshop flow

| Section | Topic |
|---------|-------|
| 1 | Setup |
| 2 | Embeddings |
| 3–5 | Load, chunk, and store documents |
| 6–8 | Retrieve context and generate answers |
| 9 | Run the local chat app |

## Tools used

| Tool | Role |
|------|------|
| Python | Core language |
| LangChain | Pipeline orchestration |
| Sentence Transformers | Local embeddings |
| ChromaDB | Local vector database |
| Gemini API | Answer generation |
| Streamlit | Local chat UI |

## Notes

- Embeddings run locally after the first model download.
- Only answer generation needs the Gemini API key.
- Everything runs on your laptop — no cloud deployment required.
- For private research documents, local-only is recommended.

## Need help?

See `docs/SETUP_GUIDE.md` for troubleshooting.
