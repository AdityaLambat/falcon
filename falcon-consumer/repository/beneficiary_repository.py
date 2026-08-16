class BeneficiaryRepository:

    INSERT_QUERY = """
        INSERT INTO beneficiary (
            beneficiary_id,
            account_id,
            beneficiary_name,
            beneficiary_account_number,
            beneficiary_bank_name,
            beneficiary_ifsc_code,
            beneficiary_status,
            created_at,
            updated_at
        )
        VALUES (
            %s, %s, %s, %s, %s,
            %s, %s, %s, %s
        )
    """

    def __init__(self, connection):

        self.connection = connection

    def save(self, beneficiary):

        cursor = self.connection.cursor()

        try:

            cursor.execute(
                self.INSERT_QUERY,
                (
                    beneficiary["beneficiaryId"],
                    beneficiary["accountId"],
                    beneficiary["beneficiaryName"],
                    beneficiary["beneficiaryAccountNumber"],
                    beneficiary["beneficiaryBankName"],
                    beneficiary["beneficiaryIfscCode"],
                    beneficiary["beneficiaryStatus"],
                    beneficiary["createdAt"],
                    beneficiary["updatedAt"]
                )
            )

        finally:

            cursor.close()