from dataclasses import dataclass, field
from datetime import UTC, datetime
from typing import Optional

from models.enums.kyc_status import KycStatus
from models.enums.customer_status import CustomerStatus
from models.enums.risk_category import RiskCategory


@dataclass
class Customer:

    customerId: Optional[int]
    firstName: str
    lastName: str
    dateOfBirth: str
    mobileNumber: str
    email: str
    address: str
    city: str
    state: str
    country: str
    kycStatus: KycStatus
    customerStatus: CustomerStatus
    riskCategory: RiskCategory

    createdAt: datetime = field(default_factory=lambda: datetime.now(UTC))
    updatedAt: datetime = field(default_factory=lambda: datetime.now(UTC))