# utils/segment_cells.py

from pathlib import Path
from typing import List, Tuple
from dataclasses import dataclass

@dataclass
class Cell:
    bbox: Tuple[int,int,int,int]  # x1,y1,x2,y2
    image_path: Path

class CellSegmenter:
    def __init__(self):
        # TODO: load SAM2 or segmentation model
        self.model = None

    def segment(self, image_path: Path, table_box) -> List[Cell]:
        """
        Using SAM2 to segment table into cells.
        Placeholder: returns a single Cell covering table_box.
        """
        x1,y1,x2,y2 = table_box
        return [Cell(bbox=(x1,y1,x2,y2), image_path=image_path)]
