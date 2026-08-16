import json

from confluent_kafka import Consumer

from config.kafka_config import (
    KAFKA_BOOTSTRAP_SERVERS,
    KAFKA_TOPIC,
    KAFKA_GROUP_ID
)

from services.event_processor import EventProcessor
from services.persistence_service import PersistenceService
from services.logging_service import LoggingService


class FalconKafkaConsumer:

    def __init__(self):

        self.consumer = Consumer({
            "bootstrap.servers": KAFKA_BOOTSTRAP_SERVERS,
            "group.id": KAFKA_GROUP_ID,
            "auto.offset.reset": "earliest",
            "enable.auto.commit": False
        })

        self.consumer.subscribe([KAFKA_TOPIC])

        self.event_processor = EventProcessor()
        self.persistence_service = PersistenceService()
        self.logger = LoggingService()

    def consume(self):

        try:

            while True:

                message = self.consumer.poll(1.0)

                if message is None:
                    continue

                if message.error():
                    continue

                event = None

                try:

                    event = json.loads(
                        message.value().decode("utf-8")
                    )

                    processed_event = (
                        self.event_processor.process(event)
                    )

                    domain = processed_event["domain"]
                    payload = processed_event["payload"]
                    correlation_id = (
                        processed_event["correlationId"]
                    )

                    persisted = (
                        self.persistence_service.persist(
                            processed_event
                        )
                    )

                    if persisted:

                        record_id = self._get_record_id(
                            domain,
                            payload
                        )

                        self.consumer.commit(
                            message=message,
                            asynchronous=False
                        )

                        self.logger.info(
                            f"{record_id} persisted successfully.",
                            domain.upper(),
                            correlation_id
                        )

                    else:

                        self.consumer.commit(
                            message=message,
                            asynchronous=False
                        )

                        self.logger.info(
                            "Duplicate event ignored.",
                            domain.upper(),
                            correlation_id
                        )

                except Exception as exception:

                    correlation_id = (
                        event.get(
                            "correlationId",
                            "UNKNOWN"
                        )
                        if event
                        else "UNKNOWN"
                    )

                    event_type = (
                        event.get(
                            "eventType",
                            "UNKNOWN"
                        )
                        if event
                        else "UNKNOWN"
                    )

                    domain = self._get_domain_name(
                        event_type
                    )

                    self.logger.error(
                        f"Persistence failed. "
                        f"Reason: {exception}",
                        domain,
                        correlation_id
                    )

        except KeyboardInterrupt:

            pass

        finally:

            self.consumer.close()
            self.persistence_service.close()

    @staticmethod
    def _get_record_id(domain, payload):

        record_ids = {
            "customer": "customerId",
            "account": "accountId",
            "beneficiary": "beneficiaryId",
            "customer_device": "deviceIdentifier",
            "transaction": "transactionId"
        }

        field = record_ids.get(domain)

        if field is None:
            return "UNKNOWN"

        return payload.get(
            field,
            "UNKNOWN"
        )

    @staticmethod
    def _get_domain_name(event_type):

        domains = {
            "falcon_Customer": "CUSTOMER",
            "falcon_Account": "ACCOUNT",
            "falcon_Beneficiary": "BENEFICIARY",
            "falcon_CustomerDevice": "CUSTOMER_DEVICE",
            "falcon_Transaction": "TRANSACTION"
        }

        return domains.get(
            event_type,
            "UNKNOWN"
        )