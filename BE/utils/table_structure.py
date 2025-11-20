# utils/table_structure.py

from typing import List
from dataclasses import dataclass

@dataclass
class TableCell:
    row: int
    col: int
    text: str
    rowspan: int = 1
    colspan: int = 1

class TableReconstructor:
    def __init__(self):
        # TODO: initialize SLANet (Paddle) or other structure models
        pass

    def reconstruct(self, cells, ocr_texts) -> List[List[str]]:
        """
        Given segmented cells and OCR results, return a 2D list representing table rows/cols.
        Placeholder: returns a single-cell table with 'TODO'.
        """
        return [["TODO: integrate SLANet + OCR results to build table"]]
