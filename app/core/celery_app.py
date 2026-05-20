from celery import Celery

celery = Celery(
    "researchos",
    broker="redis://localhost:6379/0",
    backend="redis://localhost:6379/0",
    include=["app.tasks.paper_tasks"],
)
