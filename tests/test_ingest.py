from app.db.qdrant import create_collection
from app.workflows.ingest_pipeline import ingest_paper

create_collection()

result = ingest_paper(
    "storage/papers/paper.pdf"
)

print(result)