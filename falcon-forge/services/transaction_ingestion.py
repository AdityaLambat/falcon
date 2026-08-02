from config.kafka_config import EVENT_TYPE
from mapper.transaction_mapper import TransactionMapper
from services.csv_reader import CsvReader
from services.csv_validator import CsvValidator
from services.event_builder import EventBuilder
from services.publisher import Publisher
from services.logging_service import LoggingService
from services.output_writer import OutputWriter


class TransactionIngestion:

    def __init__(self):

        self.publisher = Publisher()
        self.logger = LoggingService()

        self.total_records = 0
        self.published_records = 0
        self.failed_records = 0

    def ingest_csv(self, file_path: str):

        self.logger.info("Transaction ingestion started.")

        rows = CsvReader.read(file_path)

        self.total_records = len(rows)

        for row in rows:

            try:

                CsvValidator.validate(row)

                transaction = TransactionMapper.map_to_transaction(row)

                event = EventBuilder.build(
                    event_type=EVENT_TYPE,
                    payload=transaction
                )

                metadata = self.publisher.publish(event)

                self.published_records += 1

                self.logger.info(
                    f"{transaction.transactionReference} published successfully."
                )

                OutputWriter.write_success(
                    transaction=transaction,
                    metadata=metadata
                )

            except Exception as exception:

                self.failed_records += 1

                reference = row.get("transactionReference", "UNKNOWN")

                self.logger.error(
                    f"{reference} failed. Reason : {exception}"
                )

                OutputWriter.write_failure(
                    row=row,
                    error_message=str(exception)
                )

        self.logger.info("-------------------------------------------")
        self.logger.info(f"Total Records : {self.total_records}")
        self.logger.info(f"Published     : {self.published_records}")
        self.logger.info(f"Failed        : {self.failed_records}")
        self.logger.info("-------------------------------------------")