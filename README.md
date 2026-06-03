# PDF Question Answering using RAG (Retrieval-Augmented Generation)

This project is a beginner-friendly implementation of a **RAG pipeline** using:

- PDF parsing
- Text chunking
- Sentence embeddings
- FAISS vector search
- Gemini API for answer generation

The system retrieves relevant chunks from a PDF and uses them as context for answering user queries.

---

# What is RAG?

RAG (Retrieval-Augmented Generation) improves LLM responses by:

1. Retrieving relevant information from external data
2. Supplying that information as context to the LLM
3. Generating grounded answers

Instead of relying only on the model’s memory, the model answers using retrieved document content.

---

# Technologies Used

- Python
- FAISS
- Sentence Transformers
- Gemini API
- NumPy
- PyPDF
- dotenv

---

# Project Architecture

```txt
PDF → Chunking → Embeddings → FAISS → Retrieval → Gemini → Answer
```

---

# Project Structure

```txt
RAG-Agent-Journey/
├── 1_basic_RAG/
    ├── data/
    │   ├── sample.pdf
    ├── .env
    ├── .gitignore
    ├── main.py
    ├── observations.txt
    └── requirements.txt
```

---

# Project Workflow

## 1. Extract Text from PDF

```python
reader = PdfReader("data/sample.pdf")
```

The PDF is parsed and converted into plain text.

---

## 2. Split Text into Chunks

```python
chunk_size = 500
```

The extracted text is divided into smaller chunks for semantic retrieval.

---

## 3. Create Embeddings

```python
model = SentenceTransformer("all-MiniLM-L6-v2")
```

Each chunk is converted into a vector embedding.

### Embedding Shape Example

```python
(31, 384)
```

- 31 chunks
- 384-dimensional vector for each chunk

---

## 4. Store Embeddings in FAISS

```python
index = faiss.IndexFlatL2(dimension)
```

FAISS enables fast similarity search using vector distance.

---

## 5. Retrieve Relevant Chunks

```python
distances, indices = index.search(query_embedding, k=3)
```

Top matching chunks are retrieved based on semantic similarity.

---

## 6. Generate Final Answer using Gemini

Retrieved chunks are combined into context and sent to Gemini for answer generation.

---

# Example Query

```txt
Is abortion morally just?
```

---

# Retrieved Chunks Example

The retriever fetched chunks discussing:

- Personhood
- Right to life
- Bodily autonomy
- Moral complexity of abortion

---

# Prompt Engineering Experiment

This project also explores how prompt wording affects RAG behavior.

---

## Basic Prompt

```python
prompt = f"""
Answer the question using ONLY the context below.

Context:{context}

Question:{query}
"""
```

### Output

The model generated a nuanced answer based on conflicting viewpoints found in the retrieved chunks.

---

## Grounded / Strict Prompt

```python
prompt = f"""
You are a helpful assistant.

Answer ONLY from the provided context.

If the answer is not in the context, say:
"I could not find the answer in the document."

Context:{context}

Question:{query}
"""
```

---

# Observed Behavior

Sometimes the model responded with:

```txt
I could not find the answer in the document.
```

Even though relevant information existed in the retrieved chunks.

On another run, the model answered correctly.

Example successful response:

```txt
Different philosophers answer this question differently,
and the document concludes that abortion is morally complex
because it involves conflicting rights.
```

---

# Important Learning

This demonstrates a real-world RAG challenge:

## Retrieval ≠ Guaranteed Answer Generation

Even if relevant chunks are retrieved:

- the prompt may be too restrictive
- the model may become overly cautious
- chunk quality may affect confidence
- wording of the question matters

This is an important lesson in:

- Prompt engineering
- Grounding
- Hallucination prevention
- Context design

---

# Possible Improvements

Future improvements for this project:

- Better chunking strategies
- Overlapping chunks
- Metadata storage
- Hybrid search
- Re-ranking
- Conversational memory
- LangChain integration
- LlamaIndex integration
- Streaming responses
- Web UI using Streamlit or Flask

---

# How to Run

## 1. Clone Repository

```bash
git clone https://github.com/preethamepuri/RAG-Agent-Journey.git
cd RAG-Agent-Journey/1_basic_RAG
```

---

## 2. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 3. Create `.env`

```env
GEMINI_API_KEY=your_api_key_here
```

---

## 4. Run the Project

```bash
python main.py
```

---

# Example Output

```txt
Different philosophers answer this question differently,
and the document concludes that abortion is morally complex
because it involves conflicting rights.
```

---

# What I Learned

Through this project, I learned:

- How vector embeddings work
- Semantic similarity search
- FAISS indexing
- Prompt grounding
- Hallucination prevention techniques
- Challenges in real-world RAG systems
- Context retrieval pipelines

---

# Future Goals

As part of my RAG learning journey, I plan to build:

- Conversational RAG chatbot
- Multi-PDF RAG system
- RAG with citations
- Hybrid search systems
- Agentic RAG workflows
- Streamlit-based RAG applications
- LangChain and LlamaIndex projects

---

# Author

Built as part of my Generative AI and RAG learning journey.
