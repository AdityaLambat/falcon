from dataclasses import dataclass, field
from datetime import UTC, datetime, date
from decimal import Decimal
from typing import Optional

from models.enums.account_type import AccountType
from models.enums.account_status import AccountStatus


@dataclass
class Account:

    accountId: Optional[int]
    customerId: int
    accountNumber: str
    accountType: AccountType
    branchCode: str
    ifscCode: str
    accountStatus: AccountStatus
    balance: Decimal
    openingDate: date
    lastTransactionDate: date

    createdAt: datetime = field(default_factory=lambda: datetime.now(UTC))
    updatedAt: datetime = field(default_factory=lambda: datetime.now(UTC)) 