from enum import Enum


class BeneficiaryStatus(Enum):

    ACTIVE = "Active"
    INACTIVE = "Inactive"
    BLOCKED = "Blocked"
    DELETED = "Deleted"