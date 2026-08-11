from dataclasses import dataclass, field
from datetime import UTC, datetime
from typing import Optional


@dataclass
class CustomerDevice:

    deviceId: Optional[int]
    customerId: int
    deviceIdentifier: str
    registeredAt: Optional[datetime]
    lastSeenAt: datetime
    deviceStatus: str

    createdAt: datetime = field(default_factory=lambda: datetime.now(UTC))
    updatedAt: datetime = field(default_factory=lambda: datetime.now(UTC))