class AccountRepository:

    INSERT_QUERY = """
        INSERT INTO account (
            account_id,
            customer_id,
            account_number,
            account_type,
            branch_code,
            ifsc_code,
            account_status,
            balance,
            opening_date,
            last_transaction_date,
            created_at,
            updated_at
        )
        VALUES (
            %s, %s, %s, %s,
            %s, %s, %s, %s,
            %s, %s, %s, %s
        )
    """

    def __init__(self, connection):

        self.connection = connection

    def save(self, account):

        cursor = self.connection.cursor()

        try:

            cursor.execute(
                self.INSERT_QUERY,
                (
                    account["accountId"],
                    account["customerId"],
                    account["accountNumber"],
                    account["accountType"],
                    account["branchCode"],
                    account["ifscCode"],
                    account["accountStatus"],
                    account["balance"],
                    account["openingDate"],
                    account["lastTransactionDate"],
                    account["createdAt"],
                    account["updatedAt"]
                )
            )

        finally:

            cursor.close()