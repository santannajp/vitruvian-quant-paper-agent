import uuid

from qdrant_client.models import PointStruct

from app.db.qdrant import (
    client,
    COLLECTION_NAME,
)
from app.parsers.pdf_parser import extract_text
from app.rag.chunker import chunk_sections
from app.rag.embedder import embed_chunks


def ingest_paper(pdf_path: str):

    text = extract_text(pdf_path)

    chunks = chunk_sections(text)

    chunk_texts = [
        chunk["content"]
        for chunk in chunks
    ]

    embeddings = embed_chunks(chunk_texts)

    points = []

    for chunk, embedding in zip(chunks, embeddings):

        point = PointStruct(
            id=str(uuid.uuid4()),
            vector=embedding,
            payload={
                "section": chunk["section"],
                "content": chunk["content"],
            }
        )

        points.append(point)

    client.upsert(
        collection_name=COLLECTION_NAME,
        points=points
    )

    return {
        "status": "success",
        "chunks": len(chunks)
    }