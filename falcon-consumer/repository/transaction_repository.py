class TransactionRepository:

    INSERT_QUERY = """
        INSERT INTO transaction (
            transaction_id,
            account_id,
            beneficiary_id,
            device_identifier,
            transaction_reference,
            channel,
            transaction_type,
            amount,
            transaction_status,
            created_at,
            updated_at
        )
        VALUES (
            %s, %s, %s, %s, %s,
            %s, %s, %s, %s, %s, %s
        )
    """

    def __init__(self, connection):

        self.connection = connection

    def save(self, transaction):

        cursor = self.connection.cursor()

        try:

            cursor.execute(
                self.INSERT_QUERY,
                (
                    transaction["transactionId"],
                    transaction["accountId"],
                    transaction["beneficiaryId"],
                    transaction["deviceIdentifier"],
                    transaction["transactionReference"],
                    transaction["channel"],
                    transaction["transactionType"],
                    transaction["amount"],
                    transaction["transactionStatus"],
                    transaction["createdAt"],
                    transaction["updatedAt"]
                )
            )

        finally:

            cursor.close()