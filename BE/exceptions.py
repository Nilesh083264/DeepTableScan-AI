# exceptions.py

class DeepTableScanException(Exception):
    """Base exception for DeepTableScan backend."""
    pass

class FileTypeNotSupported(DeepTableScanException):
    """Raised when uploaded file is not supported."""
    pass

class ProcessingError(DeepTableScanException):
    """Raised when some processing step fails."""
    pass

class ModelNotLoaded(DeepTableScanException):
    """Raised when a required ML model isn't loaded."""
    pass
