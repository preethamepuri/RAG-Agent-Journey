def build_context(retrieved_chunks):
    context = "\n\n".join(
        chunk["text"]
        for chunk in retrieved_chunks
    )
    return context