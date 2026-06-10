import numpy as np

def retrieve(query,model,index,chunks,k=5):
    query_embedding = model.encode([query])

    distances, indices = index.search(
        np.array(query_embedding),
        k = 5
    )

    retrieved_chunks = [
        chunks[idx]
        for idx in indices[0]
    ]

    return retrieved_chunks