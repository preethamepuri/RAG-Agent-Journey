# RAG-Agent-Journey

A hands-on learning journey into Retrieval-Augmented Generation (RAG), Agentic AI, and AI Engineering.

This repository documents my progression from building a basic RAG pipeline from scratch to implementing more advanced retrieval systems with metadata-aware search, overlap chunking, persistent storage, and future agentic workflows.

The primary goal of this repository is to understand how modern RAG systems work internally instead of relying solely on high-level frameworks.

---

# Repository Roadmap

## 1. Basic RAG

Location:

```txt
1_basic_RAG/
```

### Features

* Single PDF ingestion
* Fixed-size chunking
* Sentence embeddings
* FAISS vector search
* Gemini-powered answer generation
* Prompt grounding experiments

### Key Concepts Learned

* Embeddings
* Semantic similarity search
* Vector databases
* Prompt engineering
* Hallucination prevention
* Basic RAG architecture

---

## 2. Multi-PDF Metadata-Aware RAG

Location:

```txt
2_advanced_multi_pdf_RAG/
```

### Features

* Multi-document ingestion
* Metadata-aware chunk storage
* Overlap chunking
* Nomic embeddings
* Persistent FAISS storage
* Modular architecture
* Grounded answer generation

### Key Concepts Learned

* Multi-document retrieval
* Metadata management
* Retrieval debugging
* Persistent vector storage
* Project modularization
* Retrieval quality improvements

---

# Current Learning Progress

Completed:

* Basic RAG
* Multi-PDF RAG
* Metadata-aware retrieval
* Overlap chunking
* Persistent storage
* Modular architecture

In Progress:

* Retrieval evaluation
* Source citations
* Recursive chunking

Planned:

* Re-ranking
* Hybrid search
* Conversational memory
* FastAPI backend
* Streamlit UI
* LangChain
* LlamaIndex
* Agentic RAG
* Multi-agent workflows

---

# Technologies Used

* Python
* FAISS
* Sentence Transformers
* Gemini API
* Nomic Embeddings
* PyPDF
* NumPy
* dotenv

---

# Repository Structure

```txt
RAG-Agent-Journey/

├── 1_basic_RAG/
│   ├── README.md
│   └── ...
│
├── 2_multi_pdf_rag/
│   ├── README.md
│   └── ...
│
└── README.md
```

Each project contains its own detailed README explaining the implementation, architecture, experiments, and learnings.

---

# Why This Repository Exists

Most RAG tutorials focus on assembling pre-built components.

This repository focuses on understanding and implementing the underlying concepts manually, including:

* Chunking strategies
* Embedding generation
* Vector search
* Retrieval pipelines
* Context construction
* Grounded prompting
* Retrieval optimization

The goal is to develop a deeper understanding of RAG systems before moving into higher-level frameworks and agentic architectures.

---

# Future Roadmap

### Retrieval Engineering

* Source citations
* Recursive chunking
* Metadata filtering
* Re-ranking
* Hybrid search
* Retrieval evaluation

### Production Engineering

* FastAPI backend
* Streamlit frontend
* Persistent databases
* Deployment

### Agentic AI

* Conversational RAG
* Tool-using agents
* Multi-agent systems
* LangGraph workflows
* Research assistants

---

# Author

Built as part of my Generative AI, RAG, and Agentic AI learning journey.

Always learning, experimenting, and iterating.
