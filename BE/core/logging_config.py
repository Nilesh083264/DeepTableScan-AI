# core/logging_config.py

from loguru import logger
import sys
from pathlib import Path
from .config import settings

LOG_FILE = Path("logs/app.log")
LOG_FILE.parent.mkdir(parents=True, exist_ok=True)

logger.remove()
logger.add(sys.stdout, level="INFO")
logger.add(str(LOG_FILE), rotation="10 MB", retention="10 days", level="DEBUG")
