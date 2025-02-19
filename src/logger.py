import logging
import os
from datetime import datetime

LOG_DIR = os.path.join(os.path.dirname(__file__), 'log')
LOG_FILE = os.path.join(LOG_DIR, 'log.txt')

# Ensure the log directory exists
os.makedirs(LOG_DIR, exist_ok=True)

def get_logger(name: str) -> logging.Logger:
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    file_handler = logging.FileHandler(LOG_FILE)
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)
    return logger

if __name__=='__main__':
    logger=get_logger(__name__)
    logger.info("This is an info message")
    logger.debug("This is a debug message")
    logger.error("This is an error message")
    logger.warning("This is a warning message")
    logger.critical("This is a critical message")
    logger.exception("This is an exception message")