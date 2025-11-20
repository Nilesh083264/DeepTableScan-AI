# utils/pdf_to_image.py

from pdf2image import convert_from_path
from pathlib import Path
from typing import List

class PDFConverter:
    def __init__(self, dpi: int = 300):
        self.dpi = dpi

    def convert(self, pdf_path: Path, out_dir: Path) -> List[Path]:
        out_dir.mkdir(parents=True, exist_ok=True)
        pil_images = convert_from_path(str(pdf_path), dpi=self.dpi)
        saved = []
        for i, img in enumerate(pil_images):
            out_path = out_dir / f"{pdf_path.stem}_page_{i+1}.png"
            img.save(out_path)
            saved.append(out_path)
        return saved
