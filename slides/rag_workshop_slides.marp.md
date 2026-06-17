---
marp: true
theme: default
paginate: true
header: 'RAG Workshop'
footer: 'Build Your Own RAG System'
style: |
  section {
    font-size: 28px;
  }
  h1 {
    color: #1a365d;
  }
  h2 {
    color: #2c5282;
  }
  code {
    background: #edf2f7;
  }
  blockquote {
    border-left: 4px solid #4299e1;
    padding-left: 1em;
    color: #4a5568;
  }
---

<!-- _class: lead -->

# Build Your Own RAG System from Scratch

## Talk to Any Document with AI

**Hands-on Workshop | 3 Hours**

<!-- speaker: Tell them they will build, not just watch. -->

---

## Agenda

- Why RAG exists
- Embeddings and semantic search
- Build the document pipeline
- Retrieve and generate answers
- Run a local chat app

---

## Who This Is For

- **Lecturers** building course assistants
- **Researchers** querying papers and policies
- **Practitioners** exploring AI workflows
- **Industry teams** prototyping knowledge tools

---

## What Is an LLM?

- Predicts the next token
- Strong at language tasks
- Weak at knowing **your** private documents
- Can **hallucinate** when unsure

---

## The Hallucination Problem

> *"What is our university's policy on X?"*

**LLM without your data** → confident but wrong answer

<!-- speaker: Ask the room if they have seen this. -->

---

## What Is RAG?

# Retrieval-Augmented Generation

Give the model the **right context** before it answers.

---

## RAG Architecture

```
User Question
     │
     ▼
[Embed Question] ──► [Vector Database] ──► Top-K Chunks
     │
     ▼
[Prompt: Context + Question] ──► [LLM] ──► Grounded Answer
```

**This is the key slide.** Keep it simple.

---

## Real-World Examples

- ChatGPT document tools
- Perplexity-style search
- Enterprise knowledge assistants
- Research and policy Q&A

---

## What Are Embeddings?

**Text → numbers that capture meaning**

- Similar meaning → close vectors
- `"car"` and `"vehicle"` are closer than `"car"` and `"banana"`

---

## Why Chunk Documents?

- LLMs have **context limits**
- Smaller chunks improve **retrieval precision**
- Overlap helps preserve meaning across boundaries

---

## Vector Database

- Stores embeddings
- Finds nearest **meaning**, not just keywords
- Today: **ChromaDB** on your laptop

---

## Demo Preview

**Live demo:** local app answering a question from sample documents

`streamlit run app.py`

<!-- speaker: 2 minutes max. Show, don't explain yet. -->

---

## Workshop Stack

| Tool | Role |
|------|------|
| Python | Core language |
| LangChain | Pipeline orchestration |
| Sentence Transformers | Local embeddings |
| ChromaDB | Local vector database |
| Gemini API | Answer generation |
| Streamlit | Local chat UI |

---

## Let's Build

Open the notebook:

`notebooks/01_rag_workshop.ipynb`

**Start at Section 2: Embeddings**

---

## The Retrieval Step

1. Question becomes a **vector**
2. Vector store returns **top-k** chunks
3. Those chunks become the LLM's **context**

<!-- speaker: Tie back to the embedding slide. -->

---

## Prompt Construction

```
System: Answer ONLY from the provided context.

Context:
[Chunk 1 | Source: policy.txt]
...
[Chunk 3 | Source: syllabus.txt]

Question: {user question}

Answer:
```

---

## With vs Without RAG

| Without RAG | With RAG |
|-------------|----------|
| Model guesses from training data | Model reads your documents first |
| May hallucinate | Grounded in retrieved context |
| No source trace | Sources can be shown |

---

## Local App Demo

Everything stays on **your machine**

```bash
cd rag-workshop
streamlit run app.py
```

No cloud deployment required.

---

## Use Cases by Audience

| Audience | Example |
|----------|---------|
| Lecturers | Course assistant for students |
| Researchers | Literature and policy Q&A |
| Industry | Internal FAQ prototype |

---

## Make It Yours

1. Add your own `.txt` or `.pdf` to `sample_docs/`
2. Rebuild the vector store
3. Test **3 real questions** from your field

---

## What You Built Today

- Document loader
- Chunking pipeline
- Local vector store
- Retrieval function
- RAG answer function
- Chat UI

---

## Learning Roadmap

**You are here:** RAG

**Next steps:**
- Better retrieval and citations
- AI Agents
- Fine-tuning
- Multimodal AI
- Production engineering

See `resources/ai_learning_roadmap.md`

---

## Recommended Resources

- LangChain docs: https://python.langchain.com/docs/
- Chroma docs: https://docs.trychroma.com/
- Gemini API: https://ai.google.dev/
- Hugging Face NLP course: https://huggingface.co/learn/nlp-course/

---

## Q&A

- Workshop repo: *(add your link)*
- Feedback form: *(add your link)*
- Contact: *(add your details)*

---

<!-- _class: lead -->

# Thank You

**Take the code. Build something useful in your domain.**

*Questions?*
