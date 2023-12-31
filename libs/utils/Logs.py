import logging
from datetime import datetime as time
from icecream import ic

class Logs:
    def __init__(self) -> None:

        logging.basicConfig(datefmt='%m/%d/%Y %I:%M:%S %p', encoding="utf-8", level=logging.DEBUG)
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')

        console = logging.StreamHandler()
        console.setLevel(level=logging.INFO) 
        console.setFormatter(formatter)

        file_log = logging.FileHandler(filename="logs/logging.log", encoding="utf-8")
        file_log.setLevel(level=logging.DEBUG)
        file_log.setFormatter(formatter)

        logger = logging.getLogger()
        for existing_handler in logger.handlers[:]:
            logger.removeHandler(existing_handler)

        logger.addHandler(console)
        logger.addHandler(file_log)

    def info(self, status: int, type: str, title: str, url: str) -> None:
        logger = logging.getLogger()
        logger.info(f"type: {type}")
        logger.info(f"title: {title}")
        logger.info(f"url: {url}")
        logger.info(f"status: {status}")

    def err(self, message: str, url: str) -> None:
        logger = logging.getLogger()
        logger.error(f"url: {url}")
        logger.error(f"message: {message}")