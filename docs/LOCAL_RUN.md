# Local Run Guide

Everything in this workshop runs on your laptop. No cloud deployment is required.

## 1. One-time setup

```bash
cd rag-workshop
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
```

Add your Gemini key to `.env`.

## 2. Build the knowledge base

```bash
python scripts/build_vector_store.py
```

This will:

1. Load files from `sample_docs/`
2. Split them into chunks
3. Create embeddings locally
4. Save them to `chroma_db/`

## 3. Run the notebook (learning path)

```bash
jupyter notebook notebooks/01_rag_workshop.ipynb
```

Use this during the session to explain each step.

## 4. Run the chat app (demo path)

```bash
streamlit run app.py
```

Open the URL shown in the terminal (usually http://localhost:8501).

## 5. Share on the same room Wi-Fi (optional)

If you want someone nearby to try your app without cloud hosting:

```bash
streamlit run app.py --server.address 0.0.0.0 --server.port 8501
```

Then share your laptop IP address and port. Use only on trusted networks.

## 6. Use your own documents

Replace or add files in `sample_docs/`, then rebuild:

```bash
python scripts/build_vector_store.py
```

Or use the **Build vector store** button in the Streamlit sidebar.

## 7. Reset everything

```bash
rm -rf chroma_db/
python scripts/build_vector_store.py
```


Your documents and embeddings stay on your machine. Only the final question and retrieved context are sent to the Gemini API for answer generation.
