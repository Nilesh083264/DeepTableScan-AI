# workflows/pipeline.py

from pathlib import Path
from utils.file_handler import FileHandler
from utils.pdf_to_image import PDFConverter
from utils.docx_to_image import DocxConverter
from utils.enhance_image import ImageEnhancer
from utils.detect_table import TableDetector
from utils.segment_cells import CellSegmenter
from utils.ocr_reader import OCRReader
from utils.table_structure import TableReconstructor
from utils.exporter import Exporter
from core.config import settings
from exceptions import ProcessingError
import uuid
from core.logging_config import logger

class DeepTablePipeline:
    def __init__(self):
        self.file_handler = FileHandler()
        self.pdf_conv = PDFConverter()
        self.docx_conv = DocxConverter()
        self.enhancer = ImageEnhancer()
        self.detector = TableDetector()
        self.segmenter = CellSegmenter()
        self.ocr = OCRReader()
        self.reconstructor = TableReconstructor()
        self.exporter = Exporter(settings.OUTPUT_DIR)

    def process(self, uploaded_path: Path) -> dict:
        """
        Main sync pipeline:
        1. convert input to images
        2. enhance images
        3. detect tables
        4. segment cells
        5. OCR
        6. reconstruct structure
        7. export xlsx + html
        """
        try:
            ext = uploaded_path.suffix.lower()
            working_id = uuid.uuid4().hex
            work_dir = Path("outputs") / working_id
            work_dir.mkdir(parents=True, exist_ok=True)

            image_paths = []
            if ext == ".pdf":
                image_paths = self.pdf_conv.convert(uploaded_path, work_dir)
            elif ext == ".docx":
                pdfs = self.docx_conv.convert_to_images(uploaded_path, work_dir)
                # convert those pdfs to images using pdf converter:
                for pdf in pdfs:
                    image_paths.extend(self.pdf_conv.convert(pdf, work_dir))
            else:
                # jpeg/png/etc
                image_paths = [uploaded_path]

            all_tables = []
            for img_path in image_paths:
                logger.info(f"Processing image: {img_path}")
                enhanced = self.enhancer.enhance(img_path)
                boxes = self.detector.detect(enhanced)
                for box in boxes:
                    # box is DetectedBox; convert to tuple
                    table_box = (box.x1, box.y1, box.x2, box.y2)
                    cells = self.segmenter.segment(enhanced, table_box)
                    ocr_texts = []
                    for cell in cells:
                        ocr_texts.extend(self.ocr.read_image(cell.image_path))
                    table_2d = self.reconstructor.reconstruct(cells, ocr_texts)
                    all_tables.append(table_2d)

            # For demo, just export first detected table or a placeholder.
            if not all_tables:
                table_2d = [["No tables found / pipeline placeholders"]]
            else:
                table_2d = all_tables[0]

            base_name = uploaded_path.stem
            html_path = self.exporter.to_html(table_2d, base_name)
            xlsx_path = self.exporter.to_xlsx(table_2d, base_name)

            return {
                "html": str(html_path),
                "xlsx": str(xlsx_path),
                "work_id": working_id
            }

        except Exception as e:
            logger.exception("Pipeline processing failed")
            raise ProcessingError(str(e))
