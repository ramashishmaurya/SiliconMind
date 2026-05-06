<div align="center">

# SiliconMind 🔌

### AI-Powered Semiconductor Datasheet Intelligence Agent

![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=flat&logo=python&logoColor=white)
![LangChain](https://img.shields.io/badge/LangChain-0.2+-1C3C3C?style=flat)
![Ollama](https://img.shields.io/badge/Ollama-Local_LLM-black?style=flat)
![Llama3](https://img.shields.io/badge/Meta_Llama3-8B-0064e0?style=flat)
![Streamlit](https://img.shields.io/badge/Streamlit-1.35+-FF4B4B?style=flat&logo=streamlit&logoColor=white)
![FAISS](https://img.shields.io/badge/FAISS-Vector_DB-00599C?style=flat)
![License](https://img.shields.io/badge/License-MIT-green?style=flat)

> **Upload any semiconductor datasheet. Ask anything. Get instant, accurate answers — powered by local AI. No API keys. No internet. No cost.**

[Features](#features) · [Demo](#demo) · [Installation](#installation) · [Usage](#usage) · [Architecture](#architecture) · [Roadmap](#roadmap)

</div>

---

## The Problem

Electronics engineers and chip designers spend hours manually reading through dense, 100+ page semiconductor datasheets just to find a single specification — maximum operating voltage, thermal limits, pin configurations. This is slow, error-prone, and expensive in engineering time.

## The Solution

**SiliconMind** is an AI agent that ingests semiconductor datasheets (PDFs) and lets engineers query chip specifications in plain English. It uses Retrieval-Augmented Generation (RAG) to find the most relevant sections of a datasheet and synthesizes accurate answers using a locally-running Llama3 model.

No cloud. No API key. No data leaves your machine.

---

## Features

- **PDF Intelligence** — Upload any semiconductor datasheet and instantly make it queryable
- **RAG Pipeline** — Retrieval-Augmented Generation ensures answers are grounded in the actual datasheet, not hallucinated
- **100% Local** — Powered by Ollama + Llama3. Works fully offline after setup
- **FAISS Vector Search** — Lightning-fast semantic search across thousands of datasheet chunks
- **Streamlit UI** — Clean, browser-based interface. No frontend experience needed
- **Multi-chip Support** — Load and query multiple datasheets in one session
- **Fault-aware Q&A** — Ask about operating limits, fault conditions, and safe operating areas

---

## Demo

```
User  →  "What is the maximum supply voltage for LM358N?"
Agent →  "The maximum supply voltage for the LM358N is 32V (single supply)
          or ±16V (dual supply), as specified in the Absolute Maximum Ratings
          table on page 4 of the datasheet."

User  →  "What happens if temperature exceeds 125°C?"
Agent →  "Operating above 125°C exceeds the absolute maximum junction
          temperature. This can cause permanent damage to the device,
          increased leakage current, and potential latch-up conditions."
```

---

## Architecture

```
┌─────────────────────────────────────────────────────────┐
│                     SiliconMind                          │
│                                                          │
│  ┌──────────┐    ┌──────────┐    ┌────────────────────┐ │
│  │ PDF      │───▶│ Chunking │───▶│ FAISS Vector Store │ │
│  │ Loader   │    │ Splitter │    │ (Local Embeddings) │ │
│  └──────────┘    └──────────┘    └────────────────────┘ │
│                                           │              │
│                                           ▼              │
│  ┌──────────┐    ┌──────────┐    ┌────────────────────┐ │
│  │ Streamlit│◀───│ LangChain│◀───│  Retriever         │ │
│  │ UI       │    │ Agent    │    │  (Top-K Chunks)    │ │
│  └──────────┘    └──────────┘    └────────────────────┘ │
│                        │                                 │
│                        ▼                                 │
│               ┌─────────────────┐                        │
│               │  Ollama Llama3  │                        │
│               │  (Local LLM)   │                        │
│               └─────────────────┘                        │
└─────────────────────────────────────────────────────────┘
```

---

## Tech Stack

| Layer | Technology | Purpose |
|-------|-----------|---------|
| LLM | Meta Llama3 via Ollama | Local language model for answer generation |
| Embeddings | Ollama Embeddings | Convert text chunks to vectors |
| Vector DB | FAISS (CPU) | Semantic similarity search |
| RAG Framework | LangChain 0.2+ | Agent orchestration and retrieval chain |
| PDF Parsing | PyPDF | Extract text from datasheet PDFs |
| UI | Streamlit | Web interface |
| Language | Python 3.10+ | Core application |

---

## Project Structure

```
SiliconMind/
│
├── data/
│   └── datasheets/          # Place your PDF datasheets here
│
├── faiss_index/             # Auto-generated vector database
│
├── app.py                   # Main Streamlit application
├── pdf_loader.py            # PDF ingestion and chunking pipeline
├── agent.py                 # LangChain RAG agent
├── requirements.txt         # Python dependencies
└── README.md
```

---

## Installation

### Prerequisites

- Python 3.10 or higher
- [Ollama](https://ollama.com) installed and running
- Llama3 model pulled locally

### Step 1 — Clone the repository

```bash
git clone https://github.com/yourusername/siliconmind.git
cd siliconmind
```

### Step 2 — Install Python dependencies

```bash
pip install -r requirements.txt
```

### Step 3 — Pull Llama3 model via Ollama

```bash
ollama pull llama3
```

### Step 4 — Verify Ollama is running

```bash
ollama run llama3
# Press Ctrl+D to exit after confirming it works
```

### Step 5 — Launch the app

```bash
streamlit run app.py
```

Open your browser at `http://localhost:8501`

---

## Usage

1. **Upload a datasheet** — Click "Browse files" in the sidebar and select a semiconductor PDF (e.g., LM358N, ATmega328P, STM32F4)
2. **Process the PDF** — Click "Process karo" and wait while the RAG pipeline indexes the document
3. **Ask questions** — Use the quick-action buttons or type your own query
4. **Get answers** — SiliconMind retrieves relevant sections and generates a precise answer

### Example queries

```
"What is the absolute maximum supply voltage?"
"What are the recommended operating conditions?"
"Explain the pin configuration."
"What is the maximum output current?"
"What happens if the input exceeds VCC?"
"List all fault conditions mentioned in the datasheet."
```

---

## Requirements

```
langchain>=0.2.0
langchain-community>=0.2.0
langchain-ollama>=0.1.0
faiss-cpu>=1.7.4
pypdf>=3.0.0
streamlit>=1.35.0
python-dotenv>=1.0.0
```

---

## Roadmap

- [x] Single PDF ingestion and Q&A
- [x] Local LLM via Ollama — zero API cost
- [x] FAISS vector store with persistent index
- [ ] Multi-PDF support — query across multiple datasheets
- [ ] Fault diagnosis agent — compare live parameters vs datasheet limits
- [ ] Export answers as PDF report
- [ ] Support for SPICE model files
- [ ] REST API endpoint for integration with EDA tools

---

## Why This Project?

This project was built to demonstrate practical AI engineering skills in the semiconductor domain — specifically:

- **RAG pipeline design** from scratch using LangChain
- **Local LLM deployment** using Ollama (no cloud dependency)
- **Vector database** implementation with FAISS
- **Domain-specific AI** applied to electronics engineering
- **Production-ready code** structure with clean separation of concerns

Built as part of a portfolio targeting AI/ML engineering roles in the semiconductor and electronics industry.

---

## License

MIT License — free to use, modify, and distribute.

---

<div align="center">

Built with Python, LangChain, and Llama3 · by [Your Name](https://github.com/yourusername)

</div>
