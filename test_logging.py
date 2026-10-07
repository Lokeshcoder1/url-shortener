import logging
from app.core.logging import setup_logging

setup_logging()

logger=logging.getLogger("url-shortener")
logger.info("Application started")
logger.warning("This is a warning")
logger.error("This is an error")

