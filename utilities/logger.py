import logging
import os
from datetime import datetime

def get_logger():
    log_folder = os.path.join(os.getcwd(), "Logs")
    os.makedirs(log_folder, exist_ok=True)

    log_file = os.path.join(log_folder, f"log_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log")

    logger = logging.getLogger("automation_logger")
    logger.setLevel(logging.INFO)

    if not logger.handlers:
        file_handler = logging.FileHandler(log_file)
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

    return logger