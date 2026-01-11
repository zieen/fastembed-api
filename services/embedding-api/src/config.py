from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    DEFAULT_DENSE_MODEL: str = "BAAI/bge-small-en-v1.5"
    DEFAULT_SPARSE_MODEL: str = "prithivida/Splade_PP_en_v1"
    
    class Config:
        env_file = ".env"

settings = Settings()
