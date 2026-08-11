from models.domain.beneficiary import Beneficiary
from models.enums.beneficiary_status import BeneficiaryStatus


class BeneficiaryMapper:

    @staticmethod
    def map_to_beneficiary(row):

        return Beneficiary(
            beneficiaryId=int(row["beneficiaryId"]),
            accountId=int(row["accountId"]),
            beneficiaryName=row["beneficiaryName"],
            beneficiaryAccountNumber=row["beneficiaryAccountNumber"],
            beneficiaryBankName=row["beneficiaryBankName"],
            beneficiaryIfscCode=row["beneficiaryIfscCode"],
            beneficiaryStatus=BeneficiaryStatus(
                row["beneficiaryStatus"]
            )
        )