from datetime import UTC, datetime
from decimal import Decimal

from models.domain.transaction import Transaction
from models.enums.channel import Channel
from models.enums.transaction_status import TransactionStatus
from models.enums.transaction_type import TransactionType


class TransactionGenerator:

    @staticmethod
    def generate() -> Transaction:

        return Transaction(
            transactionId=None,
            accountId=1,
            beneficiaryId=1,
            deviceIdentifier="DEVICE001",
            transactionReference="TXN000001",
            channel=Channel.UPI,
            transactionType=TransactionType.DEBIT,
            amount=Decimal("1000.00"),
            transactionStatus=TransactionStatus.PENDING,
            createdAt=datetime.now(UTC),
            updatedAt=datetime.now(UTC)
        )