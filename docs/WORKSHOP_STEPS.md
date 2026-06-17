# Step-by-Step Workshop Build Guide

Follow this order during the session. Each step maps to one concept and one file.

---

## Step 0: Before the room arrives

**Goal:** Make sure your machine works.

```bash
cd rag-workshop
source .venv/bin/activate
cp .env.example .env   # add GEMINI_API_KEY
python scripts/build_vector_store.py
pytest tests/ -v
streamlit run app.py
```

You should see the chat app in your browser.

---

## Step 1: Explain the problem (Slides 1-11)

**Goal:** Why RAG exists.

**Say in plain language:**

1. LLMs are good at language.
2. They do not know your private documents.
3. RAG retrieves the right text first, then asks the LLM to answer.

**Show:** `docs/SLIDES_OUTLINE.md` slides 4-7.

**Optional live demo:** open `app.py` and ask one question before coding.

---

## Step 2: Setup (Notebook Section 1)

**Goal:** Everyone has the same environment.

**File:** `notebooks/01_rag_workshop.ipynb`

**Participants run:**

- imports
- `.env` check
- repo root detection

**If someone is stuck:** share `docs/SETUP_GUIDE.md`.

---

## Step 3: Embeddings (Notebook Section 2)

**Goal:** Understand semantic similarity.

**Concept:** meaning -> numbers -> compare numbers.

**Participants run the embedding demo cell.**

**Expected result:**

- exam vs test similarity is high
- exam vs banana similarity is low

**Explain:** this is how retrieval finds relevant paragraphs even when wording differs.

---

## Step 4: Load documents (Notebook Section 3)

**Goal:** Get source text into the system.

**File logic:** `rag_pipeline.py` -> `load_documents()`

**Participants fill in:**

```python
from rag_pipeline import load_documents
documents = load_documents(ROOT / "sample_docs")
```

**Explain:** PDF and TXT are supported. Metadata stores the source filename.

---

## Step 5: Chunk documents (Notebook Section 4)

**Goal:** Split long text into searchable pieces.

**File logic:** `rag_pipeline.py` -> `split_documents()`

**Participants fill in:**

```python
from rag_pipeline import split_documents
chunks = split_documents(documents)
```

**Explain:**

- chunk too large -> noisy retrieval
- chunk too small -> lost context
- overlap preserves continuity

---

## Step 6: Build local vector store (Notebook Section 5)

**Goal:** Save embeddings to disk.

**File logic:** `rag_pipeline.py` -> `build_vector_store()`

**Participants fill in:**

```python
from rag_pipeline import build_vector_store
vector_store = build_vector_store(chunks, ROOT / "chroma_db")
```

**Explain:** ChromaDB is a local database in the `chroma_db/` folder.

**Fallback:** if internet is slow, copy a prebuilt `chroma_db/` folder.

---

## Step 7: Retrieve context (Notebook Section 6)

**Goal:** Show how search works.

**Participants fill in:**

```python
question = "What is the primary purpose of government in Nigeria?"
retrieved_docs = vector_store.similarity_search(question, k=6)
```

**Explain:** we are not generating yet. We are only finding the best chunks.

---

## Step 8: Generate grounded answer (Notebook Section 7)

**Goal:** Complete the RAG loop.

**File logic:** `rag_pipeline.py` -> `answer_question()`

**Participants fill in:**

```python
from rag_pipeline import answer_question
result = answer_question(vector_store, question)
```

**Explain prompt flow:**

1. retrieve chunks
2. build context block
3. send context + question to Gemini
4. return answer + sources

This is the aha moment.

---

## Step 9: Compare without RAG (Notebook Section 8)

**Goal:** Prove why retrieval matters.

**Participants run the plain LLM cell and compare outputs.

**Expected teaching point:** without retrieval, the model may guess. With retrieval, it is grounded.

---

## Step 10: Run the local chat app (Notebook Section 9)

**Goal:** Turn the pipeline into a usable tool.

**File:** `app.py`

```bash
streamlit run app.py
```

**Explain structure:**

- `rag_pipeline.py` = brain
- `app.py` = face

Everything stays local.

---

## Step 11: Make it yours (Final 20 minutes)

**Goal:** Personalize.

**Participants choose one:**

- research paper excerpt
- course syllabus
- policy document

**Steps:**

1. add file to `sample_docs/`
2. rebuild store: `python scripts/build_vector_store.py`
3. ask 3 domain-specific questions

**Ask for 2-3 volunteers to demo.**

---

## Step 12: Close with the roadmap

**File:** `resources/ai_learning_roadmap.md`

**Message:**

- today: RAG
- next: better retrieval, agents, fine-tuning, production systems

---

## Teaching files quick reference

| When you teach... | Open this file |
|-------------------|----------------|
| Concepts | `docs/SLIDES_OUTLINE.md` |
| Live coding | `notebooks/01_rag_workshop.ipynb` |
| Backup / stuck attendees | `notebooks/01_rag_workshop_solution.ipynb` |
| How functions work | `rag_pipeline.py` |
| Local demo UI | `app.py` |
| Your private script | `docs/FACILITATOR_GUIDE.md` |
| Pre-event email | `docs/SETUP_GUIDE.md` |
| Local usage after event | `docs/LOCAL_RUN.md` |
