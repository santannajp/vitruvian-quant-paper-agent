from app.rag.retriever import retrieve

results = retrieve(
    "What is DistilBERT?"
)

for result in results:

    print("=" * 80)

    print(result["score"])

    print(result["section"])

    print(result["content"][:1000])