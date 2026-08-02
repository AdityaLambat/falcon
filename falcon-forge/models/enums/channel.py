from enum import Enum


class Channel(Enum):

    UPI = "UPI"
    IMPS = "IMPS"
    NEFT = "NEFT"
    RTGS = "RTGS"
    NET_BANKING = "Net Banking"
    MOBILE_BANKING = "Mobile Banking"
    ATM = "ATM"
    BRANCH = "Branch"
    POS = "POS"
    CHEQUE = "Cheque"