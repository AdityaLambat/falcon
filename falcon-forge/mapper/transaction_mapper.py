from decimal import Decimal

from models.domain.transaction import Transaction
from models.enums.channel import Channel
from models.enums.transaction_status import TransactionStatus
from models.enums.transaction_type import TransactionType


class TransactionMapper:

    @staticmethod
    def map_to_transaction(data: dict) -> Transaction:

        return Transaction(
            transactionId=int(data["transactionId"]) if data["transactionId"] else None,
            accountId=int(data["accountId"]),
            beneficiaryId=int(data["beneficiaryId"]) if data["beneficiaryId"] else None,
            deviceIdentifier=data["deviceIdentifier"],
            transactionReference=data["transactionReference"],
            channel=Channel(data["channel"]),
            transactionType=TransactionType(data["transactionType"]),
            amount=Decimal(data["amount"]),
            transactionStatus=TransactionStatus(data["transactionStatus"])
        )