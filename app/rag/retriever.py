#fluxo: embed pergunta > buscar chunks > montar contexto > enviar pra LLM
from app.db.qdrant import (
    client,
    COLLECTION_NAME,
)

from app.rag.embedder import embed_text


def retrieve(query: str, limit: int = 5):

    query_embedding = embed_text(query)

    response = client.query_points(
        collection_name=COLLECTION_NAME,
        query=query_embedding,
        limit=limit,
    )

    chunks = []

    for point in response.points:

        chunks.append({
            "score": point.score,
            "section": point.payload["section"],
            "content": point.payload["content"],
        })

    return chunks