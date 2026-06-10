def build_prompt(context,query):
    return f"""
You are a strict, factual assistant. 
Your task is to answer the question using text solely from the provided Context.

CRITICAL RULES:
1. Do NOT use any outside knowledge or facts not explicitly written below. 
2. If the exact sentences answering the question are missing from the Context, you MUST output word-for-word: "I could not find the answer in the document."
3. Do not attempt to summarize or extrapolate if the text cuts off.

Context: {context}
Question: {query}
Answer:
"""