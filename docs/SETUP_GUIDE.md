# Pre-Event Setup Guide

Send this to participants **3 to 5 days before** the workshop.

## What you need

- Laptop (Mac, Windows, or Linux)
- Python 3.10 or newer
- Stable internet (for first-time package/model download and Gemini API)
- A free Google Gemini API key

## Step 1: Install Python

Check your version:

```bash
python3 --version
```

You should see `3.10` or higher.

## Step 2: Download the repo

```bash
git clone <YOUR-REPO-URL>
cd rag-workshop
```

If you receive a ZIP file instead, unzip it and open the `rag-workshop` folder.

## Step 3: Create a virtual environment

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

## Step 4: Install dependencies

```bash
pip install -r requirements.txt
```

This may take a few minutes the first time.

## Step 5: Add your API key

1. Get a free key: https://aistudio.google.com/apikey
2. Copy the example env file:

```bash
cp .env.example .env
```

3. Open `.env` and replace `your_key_here` with your real key.

## Step 6: Test your setup

```bash
python scripts/build_vector_store.py
jupyter notebook notebooks/01_rag_workshop.ipynb
```

Run the first two sections of the notebook. If they work, you are ready.

Optional UI test:

```bash
streamlit run app.py
```

## Optional: bring your own document

Bring one `.txt` or `.pdf` file from your field:

- research paper
- course outline
- policy document
- technical manual

You will swap this in during the final section.

## Troubleshooting

| Problem | Fix |
|---------|-----|
| `GEMINI_API_KEY` error | Check `.env` file and restart notebook kernel |
| `pip install` fails | Upgrade pip: `python -m pip install --upgrade pip` |
| Slow first run | Normal. Embedding model downloads once |
| Streamlit port busy | Run: `streamlit run app.py --server.port 8502` |

