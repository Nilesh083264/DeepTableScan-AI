# main.py

import uvicorn
from fastapi import FastAPI
from api.routes.table_extractor import router as extractor_router
from core.config import settings
from core.logging_config import logger
from pathlib import Path

def create_app():
    app = FastAPI(title=settings.APP_NAME)
    app.include_router(extractor_router)
    # simple health endpoint
    @app.get("/health")
    def health():
        return {"status": "ok"}
    return app

app = create_app()

if __name__ == "__main__":
    # Ensure directories exist
    Path(settings.UPLOAD_DIR).mkdir(parents=True, exist_ok=True)
    Path(settings.OUTPUT_DIR).mkdir(parents=True, exist_ok=True)
    Path(settings.MODEL_DIR).mkdir(parents=True, exist_ok=True)

    logger.info("Starting DeepTableScan backend...")
    # Using uvicorn programmatically so python3 main.py works
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=False, log_level="info")
