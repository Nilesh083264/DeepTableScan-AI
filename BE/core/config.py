# core/config.py

from pydantic import BaseSettings
from pathlib import Path

class Settings(BaseSettings):
    APP_NAME: str = "DeepTableScan-AI Backend"
    UPLOAD_DIR: Path = Path("uploads")
    OUTPUT_DIR: Path = Path("outputs")
    MODEL_DIR: Path = Path("models")
    MAX_UPLOAD_SIZE_MB: int = 200

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

settings = Settings()
