# utils/enhance_image.py

from pathlib import Path

class ImageEnhancer:
    def __init__(self):
        # Init Real-ESRGAN model here if available
        # TODO: load Real-ESRGAN model or call CLI
        self.model = None

    def enhance(self, image_path: Path) -> Path:
        """
        Enhance the image and return path to enhanced image.
        For now, placeholder: returns original path.
        Replace with realesrgan inference when wiring models.
        """
        # TODO: apply Real-ESRGAN upscaling inference here.
        return image_path
