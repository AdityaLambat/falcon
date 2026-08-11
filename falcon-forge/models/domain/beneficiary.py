from dataclasses import dataclass, field
from datetime import UTC, datetime
from typing import Optional

from models.enums.beneficiary_status import BeneficiaryStatus


@dataclass
class Beneficiary:

    beneficiaryId: Optional[int]
    accountId: int
    beneficiaryName: str
    beneficiaryAccountNumber: str
    beneficiaryBankName: str
    beneficiaryIfscCode: str
    beneficiaryStatus: BeneficiaryStatus

    createdAt: datetime = field(default_factory=lambda: datetime.now(UTC))
    updatedAt: datetime = field(default_factory=lambda: datetime.now(UTC))