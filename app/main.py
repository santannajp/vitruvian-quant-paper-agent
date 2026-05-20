from fastapi import FastAPI

from app.api.routes.papers import router

app = FastAPI()

app.include_router(router)
