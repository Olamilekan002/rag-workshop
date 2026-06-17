# Slide Outline (about 25 slides)

Use slides for concepts only. Live coding stays in the notebook.

**Generated decks (ready to present):**

- `slides/index.html` — open in any browser
- `slides/rag_workshop_slides.pptx` — PowerPoint / Google Slides import
- `slides/rag_workshop_slides.marp.md` — editable Marp source
- `slides/speaker_notes.md` — full facilitator notes

See `slides/README.md` for presentation instructions.

---

## Slide 1: Title

**Build Your Own RAG System from Scratch**

Subtitle: Talk to Any Document with AI

Your name, event name, date

Speaker note: Tell them they will build, not just watch.

---

## Slide 2: Agenda

- Why RAG exists
- Embeddings and semantic search
- Build the document pipeline
- Retrieve and generate answers
- Run a local chat app

---

## Slide 3: Who this is for

- Lecturers building course assistants
- Researchers querying papers and policies
- Practitioners exploring AI workflows
- Industry teams prototyping knowledge tools

---

## Slide 4: What is an LLM?

- Predicts the next token
- Strong at language tasks
- Weak at knowing your private documents
- Can hallucinate when unsure

---

## Slide 5: The hallucination problem

Prompt: "What is our university's policy on X?"

LLM without your data -> confident but wrong answer

Speaker note: Ask room if they have seen this.

---

## Slide 6: What is RAG?

Retrieval-Augmented Generation

Give the model the right context before it answers.

---

## Slide 7: RAG architecture diagram

```
Question -> Embed -> Search Vector DB -> Top chunks
Top chunks + Question -> LLM -> Grounded answer
```

This is the key slide. Keep it simple.

---

## Slide 8: Real-world examples

- ChatGPT document tools
- Perplexity-style search
- Enterprise knowledge assistants
- Research and policy Q&A

---

## Slide 9: What are embeddings?

Text -> numbers that capture meaning

Similar meaning -> close vectors

"car" and "vehicle" are closer than "car" and "banana"

---

## Slide 10: Why chunk documents?

- LLMs have context limits
- Smaller chunks improve retrieval precision
- Overlap helps preserve meaning across boundaries

---

## Slide 11: Vector database

- Stores embeddings
- Finds nearest meaning, not just keywords
- Today: ChromaDB on your laptop

---

## Slide 12: Demo preview

Show finished local app answering a question from sample docs.

Speaker note: 2 minutes max.

---

## Slide 13: Workshop stack

- Python
- LangChain
- Sentence Transformers (local)
- ChromaDB (local)
- Gemini API (generation)
- Streamlit (local UI)

---

## Slide 14: Section transition

"Open the notebook to Section 2."

---

## Slide 15: Retrieval step

Question becomes a vector

Vector store returns top-k chunks

Speaker note: tie back to embedding slide.

---

## Slide 16: Prompt construction

Context + question + instruction:

"Answer only from the provided context."

---

## Slide 17: With vs without RAG

Side-by-side expected behavior

Without retrieval -> guess

With retrieval -> grounded answer

---

## Slide 18: Local app demo

`streamlit run app.py`

Everything stays on your machine.

---

## Slide 19: Use cases by audience

- Lecturers: course assistant
- Researchers: literature/policy assistant
- Industry: internal FAQ prototype

---

## Slide 20: Make it yours

Swap in your own document

Test 3 real questions from your field

---

## Slide 21: What you built today

- Document loader
- Chunking pipeline
- Local vector store
- Retrieval function
- RAG answer function
- Chat UI

---

## Slide 22: Learning roadmap

You are here: RAG

Next:

- Agents
- Fine-tuning
- Multimodal AI
- Production engineering

---

## Slide 23: Recommended next resources

Point to `resources/ai_learning_roadmap.md`

---

## Slide 24: Q&A

Feedback form link

Repo link

Your contact details

---

## Slide 25: Thank you

"Take the code. Build something useful in your domain."
