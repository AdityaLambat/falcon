from falcon_core.utils.correlation_id import (
    CorrelationIdGenerator
)

from config.kafka_config import EVENT_TYPE_BENEFICIARY
from mapper.beneficiary_mapper import BeneficiaryMapper
from services.csv_reader import CsvReader
from services.csv_validator import CsvValidator
from services.event_builder import EventBuilder
from services.publisher import Publisher
from falcon_core.logging.logging_service import (
    LoggingService
)


class BeneficiaryIngestion:

    def __init__(self):

        self.publisher = Publisher()
        self.logger = LoggingService()

        self.total_records = 0
        self.published_records = 0
        self.failed_records = 0

    def ingest_csv(self, file_path: str):

        self.logger.info(
            "########## Beneficiary ingestion started ##########"
        )

        rows = CsvReader.read(file_path)

        self.total_records = len(rows)

        for row in rows:

            correlation_id = CorrelationIdGenerator.generate()

            try:

                CsvValidator.validate(
                    row,
                    entity_type="beneficiary"
                )

                beneficiary = BeneficiaryMapper.map_to_beneficiary(row)

                event = EventBuilder.build(
                    event_type=EVENT_TYPE_BENEFICIARY,
                    payload=beneficiary,
                    correlation_id=correlation_id
                )

                self.publisher.publish(event)

                self.published_records += 1

                self.logger.info(
                    f"{beneficiary.beneficiaryId} published successfully.",
                    domain="BENEFICIARY",
                    correlation_id=correlation_id
                )

            except Exception as exception:

                self.failed_records += 1

                reference = row.get(
                    "beneficiaryId",
                    "UNKNOWN"
                )

                self.logger.error(
                    f"{beneficiary.beneficiaryId} failed. Reason: {exception}",
                    domain="BENEFICIARY",
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
            "########## Beneficiary ingestion completed ##########"
        )