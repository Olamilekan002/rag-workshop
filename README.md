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
│   ├── 01_rag_workshop.ipynb
│   └── 01_rag_workshop_colab.ipynb
├── sample_docs/             # Starter documents
├── slides/
│   └── rag_workshop_slides.pdf
└── docs/
    ├── SETUP_GUIDE.md       # Read this before the event
    └── LOCAL_LLM.md         # Gemini (default) or Ollama
```

## Quick start

```bash
git clone https://github.com/Olamilekan002/rag-workshop.git
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

## Google Colab (no local setup)

Open the workshop in Colab — no terminal, venv, or Jupyter install required. Add your Gemini API key in **Colab Secrets** (`GEMINI_API_KEY`).

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1piTDy4enTDSodTezcVjJ_Jg0E535uW2C?usp=sharing)

Direct link: https://colab.research.google.com/drive/1piTDy4enTDSodTezcVjJ_Jg0E535uW2C?usp=sharing

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

## After the workshop

You completed the RAG foundation. Here is a practical path forward.

### Level 1: You are here

**RAG (Retrieval-Augmented Generation)**

Skills: document loading and chunking, embeddings and vector search, prompt grounding, local prototyping.

Build next: course assistant for your students, policy Q&A bot for your office, research paper assistant for your team.

### Level 2: Better RAG

Topics: chunk size tuning, metadata filters, source citations, reranking retrieved chunks, handling "I don't know" gracefully.

Practice project: upload 10 PDFs from one domain and measure answer quality with 20 test questions.

### Level 3: AI Agents

RAG answers questions; agents take actions (search, write, call tools).

Learn: function calling, tool design, agent loops, LangGraph basics.

Practice project: research assistant that searches, summarizes, and saves notes.

### Level 4: Fine-tuning

When RAG is not enough: domain-specific language, structured output at scale, style/format control.

Learn: dataset preparation, evaluation, when fine-tuning is worth the cost.

### Level 5: Production AI

Move from prototype to reliable system: logging and monitoring, access control, privacy and governance, cost management, deployment on internal servers.

For sensitive research data, prefer on-prem/local deployment.

### Free resources

| Topic | Resource |
|-------|----------|
| LangChain docs | https://python.langchain.com/docs/ |
| Chroma docs | https://docs.trychroma.com/ |
| Gemini API | https://ai.google.dev/ |
| Hugging Face NLP course | https://huggingface.co/learn/nlp-course/ |
| Streamlit docs | https://docs.streamlit.io/ |
