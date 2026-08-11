from enum import Enum


class AccountStatus(Enum):

    ACTIVE = "Active"
    INACTIVE = "Inactive"
    FROZEN = "Frozen"
    BLOCKED = "Blocked"
    DORMANT = "Dormant"
    CLOSED = "Closed"