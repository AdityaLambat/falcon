from falcon_core.utils.correlation_id import (
    CorrelationIdGenerator
)

from config.kafka_config import EVENT_TYPE_ACCOUNT
from mapper.account_mapper import AccountMapper
from services.csv_reader import CsvReader
from services.csv_validator import CsvValidator
from services.event_builder import EventBuilder
from services.publisher import Publisher
from falcon_core.logging.logging_service import (
    LoggingService
)


class AccountIngestion:

    def __init__(self):

        self.publisher = Publisher()
        self.logger = LoggingService()

        self.total_records = 0
        self.published_records = 0
        self.failed_records = 0

    def ingest_csv(self, file_path: str):

        self.logger.info(
            "########## Account ingestion started ##########"
        )

        rows = CsvReader.read(file_path)

        self.total_records = len(rows)

        for row in rows:

            correlation_id = CorrelationIdGenerator.generate()

            try:

                CsvValidator.validate(
                    row,
                    entity_type="account"
                )

                account = AccountMapper.map_to_account(row)

                event = EventBuilder.build(
                    event_type=EVENT_TYPE_ACCOUNT,
                    payload=account,
                    correlation_id=correlation_id
                )

                self.publisher.publish(event)

                self.published_records += 1

                self.logger.info(
                    f"{account.accountId} published successfully.",
                    domain="ACCOUNT",
                    correlation_id=correlation_id
                )

            except Exception as exception:

                self.failed_records += 1

                reference = row.get(
                    "accountId",
                    "UNKNOWN"
                )

                self.logger.error(
                    f"{account.accountId} failed. Reason: {exception}",
                    domain="ACCOUNT",
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
            "########## Account ingestion completed ##########"
        )