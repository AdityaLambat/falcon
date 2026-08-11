import logging
from pathlib import Path


class LoggingService:

    def __init__(self):

        self.logger = logging.getLogger("FalconConsumerLogger")

        if not self.logger.handlers:

            log_directory = Path("logs")
            log_directory.mkdir(exist_ok=True)

            handler = logging.FileHandler(
                log_directory / "consumer.log",
                encoding="utf-8"
            )

            formatter = logging.Formatter(
                "%(asctime)s | %(levelname)s | %(message)s"
            )

            handler.setFormatter(formatter)

            self.logger.addHandler(handler)
            self.logger.setLevel(logging.INFO)

    def info(
        self,
        message: str,
        domain: str,
        correlation_id: str
    ):

        self.logger.info(
            f"{domain} | "
            f"CorrelationId: {correlation_id} | "
            f"{message}"
        )

    def error(
        self,
        message: str,
        domain: str,
        correlation_id: str
    ):

        self.logger.error(
            f"{domain} | "
            f"CorrelationId: {correlation_id} | "
            f"{message}"
        )