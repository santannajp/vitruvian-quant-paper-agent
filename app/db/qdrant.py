from qdrant_client import QdrantClient

client = QdrantClient(
    url="http://localhost:6333"
    )

client.recreate_collection(
    collection_name="papers",
    vectors_config={
        "size": 384,
        "distance": "Cosine"
    }
)
    
