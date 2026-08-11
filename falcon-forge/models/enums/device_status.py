from enum import Enum


class DeviceStatus(Enum):

    ACTIVE = "Active"
    INACTIVE = "Inactive"
    BLOCKED = "Blocked"
    RETIRED = "Retired"