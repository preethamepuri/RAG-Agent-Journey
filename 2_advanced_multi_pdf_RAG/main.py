import os
from ingestion.pdf_loader import load_documents
from ingestion.chunker import create_chunks
from retrieval.embedder import create_embeddings,model
from retrieval.vector_store import build_index
from retrieval.search import retrieve
from llm.context_builder import build_context
from llm.prompts import build_prompt
from llm.client import generate_answer
from retrieval.storage_manager import save_chunks,load_chunks,save_index,load_index

INDEX_PATH = "storage/faiss.index"
CHUNKS_PATH = "storage/chunks.pkl"

# --------------------------------
# Ingestion
# --------------------------------

if os.path.exists(INDEX_PATH) and os.path.exists(CHUNKS_PATH):
    print("Loading existing index...")

    chunks = load_chunks(CHUNKS_PATH)
    index = load_index(INDEX_PATH)

else:
    print("Creating new index...")

    documents = load_documents("data")
    chunks = create_chunks(documents)
    embeddings = create_embeddings(chunks)
    index = build_index(embeddings)

    save_chunks(
        chunks,
        CHUNKS_PATH
    )

    save_index(
        index,
        INDEX_PATH
    )

# the below lines of code are written when we didnt implement persistent storage
# documents = load_documents("data")
# chunks = create_chunks(documents)
# embeddings = create_embeddings(chunks)
# index = build_index(embeddings)

# just for debugging purposes
# print("Documents:", len(documents))
# print("Chunks:", len(chunks))
# print("Embeddings type:", type(embeddings))
# print("Embeddings shape:", embeddings.shape)

print('type "exit" to stop the chat')
while True:
    # --------------------------------
    # Query
    # --------------------------------
    query = input("Ask a question: ")

    if query.lower() == "exit":
        break

    retrieved_chunks = retrieve(
        query,
        model,
        index,
        chunks
    )

    # --------------------------------
    # Context
    # --------------------------------

    context = build_context(
        retrieved_chunks
    )

    # --------------------------------
    # Prompt
    # --------------------------------

    prompt = build_prompt(
        context,
        query
    )

    # --------------------------------
    # Gemini
    # --------------------------------

    answer = generate_answer(
        prompt
    )

    print("\nAnswer:\n")
    print(answer)