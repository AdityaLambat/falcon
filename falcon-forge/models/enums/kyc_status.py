from enum import Enum


class KycStatus(Enum):

    PENDING = "Pending"
    IN_PROGRESS = "In Progress"
    VERIFIED = "Verified"
    REJECTED = "Rejected"
    EXPIRED = "Expired"