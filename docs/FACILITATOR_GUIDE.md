# Facilitator Guide

Private run-of-show for the 3-hour RAG workshop.

## Before the event

- [ ] Run `01_rag_workshop_solution.ipynb` end to end
- [ ] Run `streamlit run app.py` and test 3 questions
- [ ] Pre-build `chroma_db/` as fallback (`python scripts/build_vector_store.py`)
- [ ] Put solution notebook in a hidden tab/branch
- [ ] Share `docs/SETUP_GUIDE.md` 3-5 days early
- [ ] Create WhatsApp/Telegram troubleshooting group

## Teaching principle

Explain one idea, demo once, then let them code immediately.

Do not live-debug for more than 2 minutes. Point to the solution notebook and move on.

---

## Session map

| Time | Section | Notebook | What to say |
|------|---------|----------|-------------|
| 0:00-0:25 | Why RAG | Slides 1-11 | Problem first, demo last in this section |
| 0:25-0:45 | Embeddings | Section 2 | Use exam vs banana example |
| 0:45-1:15 | Docs + chunks + store | Sections 3-5 | Code-along, walk the room |
| 1:15-1:30 | Break | - | - |
| 1:30-2:10 | Retrieve + answer | Sections 6-8 | This is the aha moment |
| 2:10-2:40 | Local app | Section 9 + `app.py` | Show UI, not new theory |
| 2:40-3:00 | Own docs + roadmap | Own files | 2-3 volunteer demos |

---

## Opening script (2 minutes)

> Good morning everyone. In the next three hours we will build a real RAG system: the same pattern behind modern document Q&A tools.
>
> You will load documents, store them in a local vector database, retrieve the right context, and generate grounded answers with an LLM.
>
> Open `notebooks/01_rag_workshop.ipynb`. We start with setup.

---

## Section scripts

### Section 1: Setup

**Say:** "We only need one external API today: Gemini for answer generation. Embeddings run locally."

**Watch for:** missing `.env`, wrong folder, forgot to activate venv.

### Section 2: Embeddings

**Say:** "Embeddings turn text into meaning. Similar ideas become similar numbers."

**Demo moment:** exam sentence vs test sentence should score higher than exam vs banana.

**Transition:** "Now we apply this to real documents."

### Section 3-5: Document pipeline

**Say:** "RAG quality depends on how we load and chunk documents."

**Fill-in answers for starter notebook:**

```python
# Section 3
from rag_pipeline import load_documents
documents = load_documents(ROOT / "sample_docs")

# Section 4
from rag_pipeline import split_documents
chunks = split_documents(documents)

# Section 5
from rag_pipeline import build_vector_store
vector_store = build_vector_store(chunks, ROOT / "chroma_db")
```

**Watch for:** slow first embedding download, empty folder, PDF parsing errors.

**Fallback:** use prebuilt `chroma_db/` from repo.

### Section 6-8: RAG answer

**Say:** "Retrieval first, generation second. That is the whole architecture."

**Fill-in answers:**

```python
# Section 6
retrieved_docs = vector_store.similarity_search(question, k=6)

# Section 7
from rag_pipeline import answer_question
result = answer_question(vector_store, question)
```

**Aha moment:** compare plain LLM answer vs RAG answer in Section 8.

### Section 9: Local app

**Say:** "The notebook is for learning. The app is for using."

Run:

```bash
streamlit run app.py
```

Suggested demo questions (IFS 415 Enterprise Architecture):

1. "How does IFS 415 define a stakeholder?"
2. "What are the six basic elements of enterprise architecture?"
3. "What is the difference between e-Business and ERP according to this course?"
4. "What are the four key EA domains?"
5. "What is architecture defined as in this course?" (answer: structure with a vision)

---

## Timing checkpoints

- 0:45 -> should be starting Section 3
- 1:15 -> break
- 2:00 -> should be in Section 7
- 2:30 -> Streamlit app running for most people

If behind:

- give Section 5-7 fill-ins from facilitator sheet
- skip Section 8 comparison
- give prewritten `app.py` run command only

---

## Common failures

| Issue | Quick fix |
|-------|-----------|
| API key error | reopen `.env`, restart kernel |
| import error | ensure repo root is on path |
| model download slow | use prebuilt `chroma_db/` |
| Streamlit port in use | `--server.port 8502` |
| empty retrieval | rebuild vector store |

---

## Close script (2 minutes)

> You now understand the core pattern behind most document AI systems: chunk, embed, retrieve, generate.
>
> Take the code home, point it at your own documents, and explore the learning roadmap in `resources/ai_learning_roadmap.md`.

---

## Files to open during delivery

1. `notebooks/01_rag_workshop.ipynb` (shared screen)
2. `notebooks/01_rag_workshop_solution.ipynb` (your backup)
3. `app.py` terminal
4. `slides/index.html` or `slides/rag_workshop_slides.pptx` (+ `slides/speaker_notes.md`)
