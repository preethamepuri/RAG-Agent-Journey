# Multi-PDF RAG System with Metadata and Persistent Storage

This project is an upgraded Retrieval-Augmented Generation (RAG) system built from scratch using Python, FAISS, Sentence Transformers, and the Gemini API.

Unlike a basic RAG pipeline that works on a single PDF, this version supports multiple PDFs, metadata-aware retrieval, overlap chunking, and persistent vector storage.

The goal of this project was to move beyond a tutorial-level RAG system and explore the architectural concepts used in real-world document retrieval systems.

---

# Features

* Multi-PDF document ingestion
* Metadata-aware chunk storage
* Overlap chunking
* Nomic embeddings
* FAISS vector search
* Persistent index storage
* Modular project architecture
* Grounded answer generation using Gemini

---

# What is RAG?

Retrieval-Augmented Generation (RAG) combines information retrieval with Large Language Models.

Instead of relying solely on the model's training data, the system:

1. Retrieves relevant information from external documents
2. Uses the retrieved content as context
3. Generates answers grounded in that context

This significantly reduces hallucinations and allows the model to answer questions about private or custom documents.

---

# Technologies Used

* Python
* FAISS
* Sentence Transformers
* Nomic Embeddings
* Gemini API
* PyPDF
* NumPy
* dotenv
* Pickle

---

# Project Architecture

```txt
PDFs
 ↓
Metadata-Aware Chunking
 ↓
Embeddings
 ↓
FAISS
 ↓
Persistent Storage
 ↓
Retrieval
 ↓
Context Construction
 ↓
Gemini
 ↓
Answer
```

---

# Project Structure

```txt
2_multi_pdf_rag/

├── data/
│   ├── bitcoin.pdf
│   ├── sherlock_holmes.pdf
│
├── ingestion/
│   ├── pdf_loader.py
│   └── chunker.py
│
├── retrieval/
│   ├── embedder.py
│   ├── vector_store.py
│   ├── search.py
│   └── storage_manager.py
│
├── llm/
│   ├── gemini_client.py
│   ├── prompts.py
│   └── context_builder.py
│
├── storage/
│   ├── faiss.index
│   └── chunks.pkl
│
├── main.py
├── requirements.txt
└── .env
```

---

# Major Improvements over Basic RAG

## 1. Multi-PDF Support

The previous implementation only worked with a single PDF.

This version automatically loads and processes all PDFs present inside the data directory.

```python
for pdf_file in os.listdir("data"):
```

This allows the system to build a single searchable knowledge base from multiple documents.

---

## 2. Metadata-Aware Retrieval

Instead of storing chunks as plain text:

```python
"Machine Learning is a subset of AI"
```

each chunk stores additional metadata:

```python
{
    "text": chunk,
    "source": pdf_name,
    "page": page_number,
    "chunk_id": id
}
```

Metadata enables:

* Source tracking
* Page tracking
* Future citation generation
* Metadata filtering
* Better retrieval debugging

---

## 3. Overlap Chunking

Basic chunking can split important information across chunk boundaries.

To reduce information loss, this project implements overlap chunking.

Example:

```txt
Chunk 1:
Machine Learning is a subset of AI...

Chunk 2:
...subset of AI that focuses on...
```

Part of the previous chunk is repeated in the next chunk.

Benefits:

* Better semantic continuity
* Improved retrieval quality
* Reduced context fragmentation

Current configuration:

```python
chunk_size = 500
overlap = 100
```

---

## 4. Improved Embeddings

The initial RAG project used:

```python
all-MiniLM-L6-v2
```

This project upgrades to:

```python
nomic-ai/nomic-embed-text-v1.5
```

Benefits:

* Better semantic understanding
* Stronger retrieval performance
* Improved retrieval accuracy on larger document collections

---

## 5. Persistent Storage

One major limitation of many beginner RAG systems is rebuilding embeddings every time the application starts.

This project separates:

### Ingestion Phase

```txt
Load PDFs
 ↓
Chunking
 ↓
Embeddings
 ↓
FAISS Index
 ↓
Save
```

### Retrieval Phase

```txt
Load Index
 ↓
Retrieve
 ↓
Answer
```

Stored files:

```txt
storage/
├── faiss.index
├── chunks.pkl
```

This significantly reduces startup time.

---

# Retrieval Workflow

## Step 1: User Query

Example:

```txt
How does the network handle the problem of nodes leaving and rejoining?
```

---

## Step 2: Query Embedding

The question is converted into a vector embedding using the same embedding model used for document chunks.

---

## Step 3: Vector Search

FAISS searches for the most semantically similar chunks.

```python
distances, indices = index.search(...)
```

---

## Step 4: Context Construction

The retrieved chunks are combined into a single context block.

```python
context = ...
```

---

## Step 5: Grounded Generation

The context and question are passed to Gemini.

The model is instructed to answer only from the retrieved context.

```python
If the answer is not in the context,
say:
"I could not find the answer in the document."
```

This helps reduce hallucinations.

---

# Example Questions

## Bitcoin Whitepaper

Question:

```txt
How does the network handle the problem of nodes leaving and rejoining?
```

Answer:

```txt
Nodes can leave and rejoin the network at will,
accepting the longest proof-of-work chain as proof
of what happened while they were gone.
```

---

## Sherlock Holmes

Question:

```txt
What was the occupation of Jabez Wilson?
```

Answer:

```txt
Jabez Wilson began as a ship's carpenter.
```

---

# Key Learnings

Through this project, I learned:

* Multi-document retrieval systems
* Metadata-aware document processing
* Overlap chunking strategies
* Embedding model selection
* Persistent vector storage
* Modular software design
* Retrieval debugging techniques
* Grounded prompting
* Real-world RAG architecture concepts

---

# Future Improvements

Planned upgrades:

* Source citations
* Retrieval evaluation framework
* Recursive chunking
* Metadata filtering
* Re-ranking
* Hybrid search
* Conversational memory
* FastAPI backend
* Streamlit UI
* LangChain integration
* LlamaIndex integration
* Agentic RAG workflows

---

# Author

Built as part of my Generative AI, RAG, and Agentic AI learning journey.
