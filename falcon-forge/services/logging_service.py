import logging
from pathlib import Path


class LoggingService:

    def __init__(self):

        log_directory = Path("logs")
        log_directory.mkdir(exist_ok=True)

        self.logger = logging.getLogger("FalconLogger")

        if not self.logger.handlers:

            self.logger.setLevel(logging.INFO)

            formatter = logging.Formatter(
                "%(asctime)s | %(levelname)s | %(message)s"
            )

            file_handler = logging.FileHandler(
                log_directory / "ingestion.log",
                encoding="utf-8"
            )

            file_handler.setFormatter(formatter)

            self.logger.addHandler(file_handler)

    def info(self, message: str):

        self.logger.info(message)

    def error(self, message: str):

        self.logger.error(message)