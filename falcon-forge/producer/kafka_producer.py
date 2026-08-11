import json
import logging
from pathlib import Path

from confluent_kafka import Producer

from config.kafka_config import (
    KAFKA_BOOTSTRAP_SERVERS,
    KAFKA_TOPIC
)


class FalconKafkaProducer:

    def __init__(self):

        self._configure_logger()

        self.producer = Producer({
            "bootstrap.servers": KAFKA_BOOTSTRAP_SERVERS
        })

        self._current_correlation_id = "UNKNOWN"

    @staticmethod
    def _configure_logger():

        log_directory = Path("logs")
        log_directory.mkdir(exist_ok=True)

        logger = logging.getLogger("FalconKafkaLogger")

        if not logger.handlers:

            logger.setLevel(logging.INFO)

            formatter = logging.Formatter(
                "%(asctime)s | %(levelname)s | %(message)s"
            )

            file_handler = logging.FileHandler(
                log_directory / "kafka.log",
                encoding="utf-8"
            )

            file_handler.setFormatter(formatter)

            logger.addHandler(file_handler)

    @property
    def logger(self):

        return logging.getLogger("FalconKafkaLogger")

    def delivery_report(self, err, msg):

        correlation_id = self._current_correlation_id

        if err is not None:

            self.logger.error(
                f"CorrelationId: {correlation_id} | "
                f"Message delivery failed | "
                f"Topic: {msg.topic()} | "
                f"Error: {err}"
            )

        else:

            self.logger.info(
                f"CorrelationId: {correlation_id} | "
                f"Event published successfully | "
                f"Topic: {msg.topic()} | "
                f"Partition: {msg.partition()} | "
                f"Offset: {msg.offset()}"
            )

    def publish(self, event):

        self._current_correlation_id = event.get(
            "correlationId",
            "UNKNOWN"
        )

        self.producer.produce(
            topic=KAFKA_TOPIC,
            value=json.dumps(event),
            callback=self.delivery_report
        )

        self.producer.flush()