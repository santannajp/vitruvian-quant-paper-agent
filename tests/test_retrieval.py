from app.rag.retriever import retrieve

results = retrieve(
    "What is DistilBERT?"
)

for r in results:

    print("=" * 80)

    print("SCORE:", r["score"])

    print("SECTION:", r["section"])

    print(r["content"][:1000])