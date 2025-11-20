# utils/exporter.py

from pathlib import Path
import pandas as pd

class Exporter:
    def __init__(self, output_dir: Path):
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(parents=True, exist_ok=True)

    def to_html(self, table_2d, out_name: str) -> Path:
        df = pd.DataFrame(table_2d)
        out_path = self.output_dir / f"{out_name}.html"
        df.to_html(out_path, index=False, header=False)
        return out_path

    def to_xlsx(self, table_2d, out_name: str) -> Path:
        df = pd.DataFrame(table_2d)
        out_path = self.output_dir / f"{out_name}.xlsx"
        df.to_excel(out_path, index=False, header=False)
        return out_path
