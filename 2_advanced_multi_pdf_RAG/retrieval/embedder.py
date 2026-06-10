from sentence_transformers import SentenceTransformer

model = SentenceTransformer("nomic-ai/nomic-embed-text-v1.5", trust_remote_code=True) # --> a better pretrained embedding model

def create_embeddings(chunks):
    texts = [chunk["text"] for chunk in chunks]
    return model.encode(texts)