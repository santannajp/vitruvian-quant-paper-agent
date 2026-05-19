#criando a config central e instalando - uv add pydantic-settings
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
   OPENAI_API_KEY: str
   DATABASE_URL: str
   QDRANT_URL: str
   
   class Config:
       env_file = ".env"


settings = Settings()