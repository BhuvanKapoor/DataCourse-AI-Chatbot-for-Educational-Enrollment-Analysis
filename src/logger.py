import logging
from config.config import LOG_CONFIG


def setup_logger():
    """Configure and return a logger instance"""
    logging.basicConfig(
        filename=LOG_CONFIG["filename"],
        format=LOG_CONFIG["format"],
        level=LOG_CONFIG["level"],
    )
    return logging.getLogger(__name__)


logger = setup_logger()
