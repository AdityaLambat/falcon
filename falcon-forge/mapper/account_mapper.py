from datetime import datetime
from decimal import Decimal

from models.domain.account import Account
from models.enums.account_type import AccountType
from models.enums.account_status import AccountStatus


class AccountMapper:

    @staticmethod
    def map_to_account(row):

        return Account(
            accountId=int(row["accountId"]),
            customerId=int(row["customerId"]),
            accountNumber=row["accountNumber"],
            accountType=AccountType(row["accountType"]),
            branchCode=row["branchCode"],
            ifscCode=row["ifscCode"],
            accountStatus=AccountStatus(row["accountStatus"]),
            balance=Decimal(row["balance"]),
            openingDate=datetime.strptime(
                row["openingDate"],
                "%Y-%m-%d"
            ).date(),
            lastTransactionDate=datetime.strptime(
                row["lastTransactionDate"],
                "%Y-%m-%d"
            ).date()
        )