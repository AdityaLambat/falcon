from dataclasses import dataclass, field
from datetime import UTC, datetime
from decimal import Decimal
from typing import Optional

from models.enums.channel import Channel
from models.enums.transaction_status import TransactionStatus
from models.enums.transaction_type import TransactionType


@dataclass
class Transaction:

    transactionId: Optional[int]
    accountId: int
    beneficiaryId: Optional[int]
    deviceIdentifier: str
    transactionReference: str
    channel: Channel
    transactionType: TransactionType
    amount: Decimal
    transactionStatus: TransactionStatus

    createdAt: datetime = field(default_factory=lambda: datetime.now(UTC))
    updatedAt: datetime = field(default_factory=lambda: datetime.now(UTC))