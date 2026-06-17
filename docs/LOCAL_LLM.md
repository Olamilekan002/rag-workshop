# Free Local LLM Setup (Ollama)

The workshop uses **two local components**:

| Step | Tool | Cost |
|------|------|------|
| Embeddings | Sentence Transformers | Free, downloads once |
| Answer generation | **Ollama** | Free, runs on your laptop |

No Gemini API key is required when `LLM_PROVIDER=ollama` (the default).

---

## Why not Gemini?

Gemini free tier can hit quota limits (`429 RESOURCE_EXHAUSTED`), especially with:
- Deprecated models such as `gemini-2.0-flash` (retired June 2026; use `gemini-2.5-flash`)
- Shared project quotas (limits are per Google Cloud project, not per API key)
- High workshop usage

New AI Studio keys use the `AQ.` prefix (auth keys). That is normal and still free-tier eligible. Do not confuse them with Vertex keys from Google Cloud Console, which bill from the first request.

Ollama avoids all of that for live demos.

---

## Install Ollama (Mac)

```bash
brew install ollama
```

Or download from https://ollama.com

Start the Ollama app (menu bar) or run:

```bash
ollama serve
```

---

## Download a small model (recommended for workshops)

```bash
ollama pull llama3.2:1b
```

About 1.3 GB download. Good balance of speed and quality on a laptop.

**Alternatives if you have more RAM:**

| Model | Size | Command |
|-------|------|---------|
| llama3.2:1b | ~1.3 GB | `ollama pull llama3.2:1b` |
| phi3:mini | ~2.3 GB | `ollama pull phi3:mini` |
| llama3.2:3b | ~2.0 GB | `ollama pull llama3.2:3b` |

---

## Configure `.env`

```env
LLM_PROVIDER=ollama
OLLAMA_MODEL=llama3.2:1b
OLLAMA_BASE_URL=http://localhost:11434
```

---

## Test

```bash
ollama run llama3.2:1b "Say hello in one sentence."
```

Then restart Streamlit:

```bash
cd rag-workshop
source .venv/bin/activate
pip install -r requirements.txt
streamlit run app.py
```

---

## Switch back to Gemini (optional)

1. Get a key from https://aistudio.google.com/apikey (AI Studio, not Vertex)
2. In `.env`:

```env
LLM_PROVIDER=gemini
GEMINI_API_KEY=your_ai_studio_key
GEMINI_MODEL=gemini-2.5-flash
```

If you see `429` with `limit: 0`, check that `GEMINI_MODEL` is not a deprecated 2.0 model, then verify live quotas in AI Studio for your project.

---

## Workshop tip

Pre-download the Ollama model **before** the event. First pull needs internet; after that, demos work offline (except initial embedding model if not cached).
