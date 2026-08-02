import csv
from pathlib import Path


class OutputWriter:

    OUTPUT_DIRECTORY = Path("output")

    SUCCESS_FILE = OUTPUT_DIRECTORY / "success_transactions.csv"
    FAILED_FILE = OUTPUT_DIRECTORY / "failed_transactions.csv"

    @classmethod
    def write_success(cls, transaction, metadata):

        cls.OUTPUT_DIRECTORY.mkdir(exist_ok=True)

        file_exists = cls.SUCCESS_FILE.exists()

        with cls.SUCCESS_FILE.open(
                mode="a",
                newline="",
                encoding="utf-8"
        ) as file:

            writer = csv.writer(file)

            if not file_exists:

                writer.writerow([
                    "Processed At",
                    "Transaction Reference",
                    "Topic",
                    "Partition",
                    "Offset",
                    "Status"
                ])

            writer.writerow([
                transaction.createdAt.isoformat(),
                transaction.transactionReference,
                metadata["topic"],
                metadata["partition"],
                metadata["offset"],
                "Published"
            ])

    @classmethod
    def write_failure(cls, row: dict, error_message: str):

        cls.OUTPUT_DIRECTORY.mkdir(exist_ok=True)

        file_exists = cls.FAILED_FILE.exists()

        with cls.FAILED_FILE.open(
                mode="a",
                newline="",
                encoding="utf-8"
        ) as file:

            writer = csv.writer(file)

            if not file_exists:

                writer.writerow([
                    "Processed At",
                    "Transaction Reference",
                    "Error Message"
                ])

            writer.writerow([
                row.get("createdAt", ""),
                row.get("transactionReference", ""),
                error_message
            ])