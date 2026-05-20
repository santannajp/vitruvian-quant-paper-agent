from app.core.celery_app import celery
from app.workflows.ingest_pipeline import ingest_paper


@celery.task
def ingest_paper_task(pdf_path: str):

    result = ingest_paper(pdf_path)

    return result