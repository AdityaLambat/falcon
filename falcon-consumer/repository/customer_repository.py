class CustomerRepository:

    INSERT_QUERY = """
        INSERT INTO customer (
            customer_id,
            first_name,
            last_name,
            date_of_birth,
            mobile_number,
            email,
            address,
            city,
            state,
            country,
            kyc_status,
            customer_status,
            risk_category,
            created_at,
            updated_at
        )
        VALUES (
            %s, %s, %s, %s, %s,
            %s, %s, %s, %s, %s,
            %s, %s, %s, %s, %s
        )
    """

    def __init__(self, connection):

        self.connection = connection

    def save(self, customer):

        cursor = self.connection.cursor()

        try:

            cursor.execute(
                self.INSERT_QUERY,
                (
                    customer["customerId"],
                    customer["firstName"],
                    customer["lastName"],
                    customer["dateOfBirth"],
                    customer["mobileNumber"],
                    customer["email"],
                    customer["address"],
                    customer["city"],
                    customer["state"],
                    customer["country"],
                    customer["kycStatus"],
                    customer["customerStatus"],
                    customer["riskCategory"],
                    customer["createdAt"],
                    customer["updatedAt"]
                )
            )

        finally:

            cursor.close()