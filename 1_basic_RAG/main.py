from pypdf import PdfReader
from sentence_transformers import SentenceTransformer
import faiss
import numpy as np

import os
from dotenv import load_dotenv
from google import genai

# part 0 --> configuring AI model and connecting API key
load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key=api_key)

Model_NAME = "gemini-2.5-flash"

# part 1 --> extracting text from pdf 
reader = PdfReader("data/sample.pdf");

text = ""

for page in reader.pages:
    text += page.extract_text()

# print(text[:1000]) --> prints first 1000 characters

# part 2 --> splitting data into smaller chunks
chunk_size = 500

chunks = []

for i in range(0, len(text), chunk_size):
    chunk = text[i:i+chunk_size]
    chunks.append(chunk)

# print(chunks[0]) --> prints first 500 characters
# print(len(chunks)) --> prints # of chunks

# part 3 --> creating embeddings
model = SentenceTransformer("all-MiniLM-L6-v2") # --> using a pretrained embedding model

embeddings = model.encode(chunks)

# print(embeddings.shape)
# gives (31, 384) as output i.e., there are 31 chunks and each of them is stored as 384 dimension vector

# part 4 --> building vector search
dimension = embeddings.shape[1]

# faiss is a vector search engine built by meta.
# L2 in IndexFlatL2 means Euclidean distance --> "How far apart are two vectors?"
index = faiss.IndexFlatL2(dimension)

index.add(np.array(embeddings))

# print(index.ntotal)

# part 5 --> trying to retrieve relevant information
query = "Is abortion morally just?"

query_embedding = model.encode([query])

distances, indices = index.search(
    np.array(query_embedding),
    k = 3
)

# print(indices)
# print(distances)

# part 6 --> fetching relevant chunks
# for idx in indices[0]:
#     print(chunks[idx])
#     print("\n" + 100*"=" + "\n")

# part 7 --> creating context using retrieved chunks
context = "\n".join(
    [chunks[idx] for idx in indices[0]]
)

# part 8 --> combining context and query to generate prompt for llm
"""
BASIC PROMPT
Answer the question using ONLY the context below.
Context:{context}
Question:{query}
"""

# Models suffer from hallucination. So, we are upgrading our prompt to the one below.
# This is called "GROUNDING THE MODEL" --> very important in production RAG systems.

prompt = f"""
You are a helpful assistant.
Answer ONLY from the provided context.
If the answer is not in the context, say: "I could not find the answer in the document."
Context:{context}
Question:{query}
"""

response = client.models.generate_content(
    model = Model_NAME,
    contents = prompt
)

print(response.text)