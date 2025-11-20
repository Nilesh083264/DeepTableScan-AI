# services/task_manager.py

from concurrent.futures import ThreadPoolExecutor
from typing import Callable
from core.logging_config import logger

class TaskManager:
    def __init__(self, max_workers: int = 2):
        self.executor = ThreadPoolExecutor(max_workers=max_workers)

    def submit(self, fn: Callable, *args, **kwargs):
        future = self.executor.submit(fn, *args, **kwargs)
        logger.info("Task submitted to background executor")
        return future
