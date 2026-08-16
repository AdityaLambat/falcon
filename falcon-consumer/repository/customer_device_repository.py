class CustomerDeviceRepository:

    INSERT_QUERY = """
        INSERT INTO customer_device (
            device_identifier,
            customer_id,
            registered_at,
            last_seen_at,
            device_status,
            created_at,
            updated_at
        )
        VALUES (
            %s, %s, %s, %s,
            %s, %s, %s
        )
    """

    def __init__(self, connection):

        self.connection = connection

    def save(self, device):

        cursor = self.connection.cursor()

        try:

            cursor.execute(
                self.INSERT_QUERY,
                (
                    device["deviceIdentifier"],
                    device["customerId"],
                    device["registeredAt"],
                    device["lastSeenAt"],
                    device["deviceStatus"],
                    device["createdAt"],
                    device["updatedAt"]
                )
            )

        finally:

            cursor.close()