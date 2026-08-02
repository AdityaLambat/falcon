from enum import Enum


class TransactionStatus(Enum):

    PENDING = "Pending"
    SUCCESS = "Success"
    BLOCKED = "Blocked"
    DECLINED = "Declined"
    FAILED = "Failed"
    REVERSED = "Reversed"