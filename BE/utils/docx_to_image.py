# utils/docx_to_image.py

from docx2pdf import convert as docx2pdf_convert  # optional
from pathlib import Path
import subprocess
from typing import List

class DocxConverter:
    def convert_to_images(self, docx_path: Path, out_dir: Path) -> List[Path]:
        """
        Simple approach: convert docx -> pdf (requires libreoffice or docx2pdf),
        then pdf -> images using pdf_to_image.
        """
        out_dir.mkdir(parents=True, exist_ok=True)
        pdf_path = out_dir / f"{docx_path.stem}.pdf"
        # Option A: docx2pdf (Windows/MSOffice required) - may not work on Linux
        # Option B: libreoffice -- convert to pdf using CLI
        subprocess.run([
            "libreoffice", "--headless", "--convert-to", "pdf", "--outdir",
            str(out_dir), str(docx_path)
        ], check=True)
        # return a list of images using pdf_to_image later
        return [pdf_path]
