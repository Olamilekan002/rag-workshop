# LLM Setup: Gemini or Ollama

The workshop supports **two answer-generation options**:

| Provider | Default? | Cost | Best for |
|----------|----------|------|----------|
| **Gemini** | Yes | Free tier (API key) | Workshop default, cloud answers |
| **Ollama** | No | Free, local | Offline demos, no API key |

Embeddings always run locally with Sentence Transformers (free, downloads once).

---

## Option 1: Gemini (default)

Get a free key from [Google AI Studio](https://aistudio.google.com/apikey) (not Google Cloud Vertex).

In `.env`:

```env
LLM_PROVIDER=gemini
GEMINI_API_KEY=your_ai_studio_key
GEMINI_MODEL=gemini-2.5-flash
```

New AI Studio keys use the `AQ.` prefix. That is normal and still free-tier eligible. Do not use Vertex keys from Google Cloud Console.

**If you see `429 RESOURCE_EXHAUSTED`:**
- Use `gemini-2.5-flash` (not deprecated `gemini-2.0-flash`)
- Check live quotas in AI Studio for your project
- Switch to Ollama (Option 2) for the live session

---

## Option 2: Ollama (local fallback)

Use Ollama when you want answers fully on your laptop with no API key.

### Install (Mac)

```bash
brew install ollama
```

Or download from https://ollama.com

Start the Ollama app (menu bar) or run:

```bash
ollama serve
```

### Download a small model (recommended for workshops)

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

### Configure `.env`

```env
LLM_PROVIDER=ollama
OLLAMA_MODEL=llama3.2:1b
OLLAMA_BASE_URL=http://localhost:11434
```

### Test

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

## Workshop tip

- **Default path:** Gemini with a key set before the event.
- **Backup path:** Pre-download an Ollama model before the event if you expect quota issues or want offline demos. First pull needs internet; after that, Ollama runs locally.
