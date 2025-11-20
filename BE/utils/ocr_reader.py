# utils/ocr_reader.py

from pathlib import Path
from typing import List
from dataclasses import dataclass

@dataclass
class OCRText:
    bbox: tuple
    text: str
    confidence: float

class OCRReader:
    def __init__(self):
        # TODO: initialize PaddleOCR here
        # Example:
        # from paddleocr import PaddleOCR
        # self.ocr = PaddleOCR(use_angle_cls=True, lang='en')
        self.ocr = None

    def read_image(self, image_path: Path) -> List[OCRText]:
        """
        Use PaddleOCR to read text in the image. Placeholder returns empty list.
        """
        # TODO: call self.ocr.ocr(...) and parse results
        return []
