from datetime import datetime

from models.domain.customer import Customer
from models.enums.kyc_status import KycStatus
from models.enums.customer_status import CustomerStatus
from models.enums.risk_category import RiskCategory


class CustomerMapper:

    @staticmethod
    def map_to_customer(row):

        return Customer(
            customerId=int(row["customerId"]),
            firstName=row["firstName"],
            lastName=row["lastName"],
            dateOfBirth=datetime.strptime(row["dateOfBirth"],"%Y-%m-%d").date(),
            mobileNumber=row["mobileNumber"],
            email=row["email"],
            address=row["address"],
            city=row["city"],
            state=row["state"],
            country=row["country"],
            kycStatus=KycStatus(row["kycStatus"]),
            customerStatus=CustomerStatus(row["customerStatus"]),
            riskCategory=RiskCategory(row["riskCategory"])
        )