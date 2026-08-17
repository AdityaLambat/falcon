import logging
from pathlib import Path


class LoggingService:

    LOGGER_NAME = "FalconLogger"
    LOG_DIRECTORY = Path("logs")
    LOG_FILE = "falcon.log"

    def __init__(self):

        self.LOG_DIRECTORY.mkdir(
            exist_ok=True
        )

        self.logger = logging.getLogger(
            self.LOGGER_NAME
        )

        self._configure()

    def _configure(self):

        if self.logger.handlers:
            return

        self.logger.setLevel(
            logging.INFO
        )

        formatter = logging.Formatter(
            "%(asctime)s | %(levelname)s | %(message)s"
        )

        file_handler = logging.FileHandler(
            self.LOG_DIRECTORY / self.LOG_FILE,
            encoding="utf-8"
        )

        file_handler.setFormatter(
            formatter
        )

        self.logger.addHandler(
            file_handler
        )

    def info(
        self,
        message,
        domain=None,
        correlation_id=None
    ):

        self.logger.info(
            self._format_message(
                message,
                domain,
                correlation_id
            )
        )

    def error(
        self,
        message,
        domain=None,
        correlation_id=None
    ):

        self.logger.error(
            self._format_message(
                message,
                domain,
                correlation_id
            )
        )

    def warning(
        self,
        message,
        domain=None,
        correlation_id=None
    ):

        self.logger.warning(
            self._format_message(
                message,
                domain,
                correlation_id
            )
        )

    @staticmethod
    def _format_message(
        message,
        domain,
        correlation_id
    ):

        parts = []

        if domain:
            parts.append(str(domain))

        if correlation_id:
            parts.append(
                f"CorrelationId: {correlation_id}"
            )

        parts.append(str(message))

        return " | ".join(parts)