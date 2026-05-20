from pathlib import Path

from fastapi import APIRouter
from fastapi import UploadFile
from fastapi import File

from app.tasks.paper_tasks import (
    ingest_paper_task
)

router = APIRouter()

UPLOAD_DIR = Path("storage/papers")

UPLOAD_DIR.mkdir(
    parents=True,
    exist_ok=True
)


@router.post("/upload")
async def upload_paper(
    file: UploadFile = File(...)
):

    file_path = UPLOAD_DIR / file.filename

    with open(file_path, "wb") as buffer:

        content = await file.read()

        buffer.write(content)

    ingest_paper_task.delay(
        str(file_path)
    )

    return {
        "status": "processing",
        "file": file.filename
    }