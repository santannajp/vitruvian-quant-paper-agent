from app.rag.rag_pipeline import ask_paper

response = ask_paper(
    "What is DistilBERT?"
)

print(response)