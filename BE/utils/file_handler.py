# utils/file_handler.py

import shutil
from pathlib import Path
from fastapi import UploadFile
from core.config import settings
from exceptions import FileTypeNotSupported

ALLOWED_EXT = {".pdf", ".png", ".jpg", ".jpeg", ".docx", ".tiff", ".bmp"}

class FileHandler:
    def __init__(self, upload_dir: Path = settings.UPLOAD_DIR):
        self.upload_dir = Path(upload_dir)
        self.upload_dir.mkdir(parents=True, exist_ok=True)

    def save_upload(self, upload_file: UploadFile) -> Path:
        ext = Path(upload_file.filename).suffix.lower()
        if ext not in ALLOWED_EXT:
            raise FileTypeNotSupported(f"Extension {ext} not allowed.")
        dest = self.upload_dir / upload_file.filename
        with dest.open("wb") as buffer:
            shutil.copyfileobj(upload_file.file, buffer)
        return dest
