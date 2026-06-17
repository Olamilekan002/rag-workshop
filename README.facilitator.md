# RAG Workshop: Build Your Own Document Q&A System (Facilitator copy)

Local facilitator README — not pushed to the participant repo.

See `README.md` for the participant-facing version on GitHub.

## Full repo layout (local)

```
rag-workshop/
├── README.md
├── requirements.txt
├── .env.example
├── rag_pipeline.py
├── app.py
├── scripts/build_vector_store.py
├── notebooks/
│   ├── 01_rag_workshop.ipynb
│   └── 01_rag_workshop_solution.ipynb
├── sample_docs/
├── docs/
│   ├── SETUP_GUIDE.md
│   ├── LOCAL_RUN.md
│   ├── FACILITATOR_GUIDE.md
│   ├── WORKSHOP_STEPS.md
│   └── SLIDES_OUTLINE.md
├── slides/
└── resources/
```

## Facilitator quick start

```bash
cd rag-workshop
source .venv/bin/activate
jupyter notebook notebooks/01_rag_workshop_solution.ipynb
streamlit run app.py
open slides/index.html
```

## Workshop flow (3 hours)

| Time | Section | Artifact |
|------|---------|----------|
| 0:00-0:25 | Why RAG exists | slides/index.html |
| 0:25-0:45 | Embeddings | Notebook Section 2 |
| 0:45-1:15 | Load, chunk, store | Notebook Sections 3-5 |
| 1:15-1:30 | Break | - |
| 1:30-2:10 | Retrieve + generate | Notebook Sections 6-8 |
| 2:10-2:40 | Local chat app | streamlit run app.py |
| 2:40-3:00 | Make it yours | Own docs + roadmap |
