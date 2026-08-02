from decimal import Decimal

from models.enums.channel import Channel
from models.enums.transaction_status import TransactionStatus
from models.enums.transaction_type import TransactionType


class CsvValidator:

    REQUIRED_FIELDS = [
        "accountId",
        "beneficiaryId",
        "deviceIdentifier",
        "transactionReference",
        "channel",
        "transactionType",
        "amount",
        "transactionStatus"
    ]

    @staticmethod
    def validate(data: dict):

        CsvValidator._validate_required_fields(data)
        CsvValidator._validate_amount(data)
        CsvValidator._validate_channel(data)
        CsvValidator._validate_transaction_type(data)
        CsvValidator._validate_transaction_status(data)

    @staticmethod
    def _validate_required_fields(data: dict):

        for field in CsvValidator.REQUIRED_FIELDS:

            if field not in data or not data[field]:
                raise ValueError(f"{field} is mandatory.")

    @staticmethod
    def _validate_amount(data: dict):

        try:
            Decimal(data["amount"])
        except Exception:
            raise ValueError("Invalid amount.")

    @staticmethod
    def _validate_channel(data: dict):

        Channel(data["channel"])

    @staticmethod
    def _validate_transaction_type(data: dict):

        TransactionType(data["transactionType"])

    @staticmethod
    def _validate_transaction_status(data: dict):

        TransactionStatus(data["transactionStatus"])