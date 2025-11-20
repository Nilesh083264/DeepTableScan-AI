# utils/detect_table.py

from pathlib import Path
from typing import List
from dataclasses import dataclass

@dataclass
class DetectedBox:
    x1: int
    y1: int
    x2: int
    y2: int
    label: str
    score: float

class TableDetector:
    def __init__(self):
        # TODO: Load DocLayout-YOLO weights here
        self.model = None

    def detect(self, image_path: Path) -> List[DetectedBox]:
        """
        Run table detection and return bounding boxes for tables and maybe cells.
        For now returns a placeholder single box covering the whole image.
        Replace with DocLayout-YOLO inference.
        """
        from PIL import Image
        img = Image.open(image_path)
        w, h = img.size
        return [DetectedBox(0, 0, w, h, label="table", score=1.0)]
