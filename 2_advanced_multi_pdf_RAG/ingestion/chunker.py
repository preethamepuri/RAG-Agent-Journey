def create_chunks(documents,chunk_size=1000,overlap=200):
    
    chunks = []

    chunk_id = 0

    for doc in documents:
        page_number = doc["page"]
        source = doc["source"]
        text = doc["text"]
        for i in range(0, len(text), chunk_size-overlap):
            chunk = text[i:i+chunk_size]
            chunks.append({
                "text": chunk,
                "page": page_number,
                "source": source,
                "chunk_id": chunk_id
            })
            chunk_id += 1
    
    return chunks