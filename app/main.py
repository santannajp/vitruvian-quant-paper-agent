from fastapi import FastAPI

app = FastAPI()

#criando api basica para testar se está funcionando e rodando com uvicorn
@app.get("/")
def health():
    return {"status": "ok"}
