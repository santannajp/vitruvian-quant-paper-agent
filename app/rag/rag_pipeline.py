from app.rag.retriever import retrieve
from app.services.llm import ask_llm


def ask_paper(question: str):

    chunks = retrieve(question)

    context = "\n\n".join([
        chunk["content"]
        for chunk in chunks
    ])

    prompt = f"""
You are a financial AI researcher.

Answer the question using ONLY
the provided context.

CONTEXT:
{context}

QUESTION:
{question}
"""

    answer = ask_llm(prompt)

    return answer