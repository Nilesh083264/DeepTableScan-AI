# api/routes/table_extractor.py

from fastapi import APIRouter, UploadFile, File, HTTPException
from pathlib import Path
from workflows.pipeline import DeepTablePipeline
from core.config import settings
from exceptions import FileTypeNotSupported, ProcessingError
from core.logging_config import logger

router = APIRouter(prefix="/extract", tags=["extract"])
pipeline = DeepTablePipeline()

@router.post("/table")
async def extract_table(file: UploadFile = File(...)):
    try:
        # save file
        from utils.file_handler import FileHandler
        fh = FileHandler()
        saved_path = fh.save_upload(file)
        logger.info(f"Saved upload to {saved_path}")

        # process
        res = pipeline.process(Path(saved_path))
        return {"status":"success", "result": res}

    except FileTypeNotSupported as e:
        raise HTTPException(status_code=400, detail=str(e))
    except ProcessingError as e:
        raise HTTPException(status_code=500, detail=str(e))
    except Exception as e:
        logger.exception("Unhandled error in /extract/table")
        raise HTTPException(status_code=500, detail="Internal server error")
