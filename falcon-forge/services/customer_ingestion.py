from uuid import uuid4

from config.kafka_config import EVENT_TYPE_CUSTOMER
from mapper.customer_mapper import CustomerMapper
from services.csv_reader import CsvReader
from services.csv_validator import CsvValidator
from services.event_builder import EventBuilder
from services.publisher import Publisher
from services.logging_service import LoggingService


class CustomerIngestion:

    def __init__(self):

        self.publisher = Publisher()
        self.logger = LoggingService()

        self.total_records = 0
        self.published_records = 0
        self.failed_records = 0

    def ingest_csv(self, file_path: str):

        self.logger.info(
            "########## CUSTOMER ingestion started ##########"
        )

        rows = CsvReader.read(file_path)

        self.total_records = len(rows)

        for row in rows:

            correlation_id = str(uuid4())

            try:

                CsvValidator.validate(
                    row,
                    entity_type="customer"
                )

                customer = CustomerMapper.map_to_customer(row)

                event = EventBuilder.build(
                    event_type=EVENT_TYPE_CUSTOMER,
                    payload=customer,
                    correlation_id=correlation_id
                )

                self.publisher.publish(event)

                self.published_records += 1

                self.logger.info(
                    f"{customer.customerId} published successfully.",
                    domain="CUSTOMER",
                    correlation_id=correlation_id
                )

            except Exception as exception:

                self.failed_records += 1

                reference = row.get(
                    "customerId",
                    "UNKNOWN"
                )

                self.logger.error(
                    f"{customer.customerId} failed. Reason: {exception}",
                    domain="CUSTOMER",
                    correlation_id=correlation_id
                )

        self.logger.info("-------------------------------------------")
        self.logger.info(
            f"Total Records : {self.total_records}"
        )
        self.logger.info(
            f"Published     : {self.published_records}"
        )
        self.logger.info(
            f"Failed        : {self.failed_records}"
        )
        self.logger.info("-------------------------------------------")


        self.logger.info(
            "########## CUSTOMER ingestion completed ##########"
        )