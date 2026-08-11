import logging


class LoggingService:

    def __init__(self):

        self.logger = logging.getLogger("FalconIngestion")

        if not self.logger.handlers:

            handler = logging.FileHandler(
                "logs/ingestion.log",
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
        domain: str = None,
        correlation_id: str = None
    ):

        self._log(
            logging.INFO,
            message,
            domain,
            correlation_id
        )

    def error(
        self,
        message: str,
        domain: str = None,
        correlation_id: str = None
    ):

        self._log(
            logging.ERROR,
            message,
            domain,
            correlation_id
        )

    def _log(
        self,
        level,
        message,
        domain=None,
        correlation_id=None
    ):

        parts = []

        if domain:
            parts.append(domain)

        if correlation_id:
            parts.append(
                f"CorrelationId: {correlation_id}"
            )

        parts.append(message)

        self.logger.log(
            level,
            " | ".join(parts)
        )