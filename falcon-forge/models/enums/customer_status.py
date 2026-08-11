from enum import Enum


class CustomerStatus(Enum):

    ACTIVE = "Active"
    INACTIVE = "Inactive"
    BLOCKED = "Blocked"
    SUSPENDED = "Suspended"
    CLOSED = "Closed"