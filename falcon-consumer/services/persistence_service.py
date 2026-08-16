from database.connection import DatabaseConnection

from repository.processed_event_repository import (
    ProcessedEventRepository
)

from repository.customer_repository import (
    CustomerRepository
)

from repository.account_repository import (
    AccountRepository
)

from repository.beneficiary_repository import (
    BeneficiaryRepository
)

from repository.customer_device_repository import (
    CustomerDeviceRepository
)

from repository.transaction_repository import (
    TransactionRepository
)


class PersistenceService:

    def __init__(self):

        self.database = DatabaseConnection()

        connection = self.database.get_connection()

        self.processed_event_repository = (
            ProcessedEventRepository(connection)
        )

        self.customer_repository = (
            CustomerRepository(connection)
        )

        self.account_repository = (
            AccountRepository(connection)
        )

        self.beneficiary_repository = (
            BeneficiaryRepository(connection)
        )

        self.customer_device_repository = (
            CustomerDeviceRepository(connection)
        )

        self.transaction_repository = (
            TransactionRepository(connection)
        )

    def persist(self, event):

        connection = self.database.get_connection()

        try:

            # First register the event for idempotency.
            is_new_event = (
                self.processed_event_repository.save(event)
            )

            if not is_new_event:

                connection.rollback()

                return False

            domain = event["domain"]
            payload = event["payload"]

            if domain == "customer":

                self.customer_repository.save(
                    payload
                )

            elif domain == "account":

                self.account_repository.save(
                    payload
                )

            elif domain == "beneficiary":

                self.beneficiary_repository.save(
                    payload
                )

            elif domain == "customer_device":

                self.customer_device_repository.save(
                    payload
                )

            elif domain == "transaction":

                self.transaction_repository.save(
                    payload
                )

            else:

                raise ValueError(
                    f"Unsupported domain: {domain}"
                )

            connection.commit()

            return True

        except Exception:

            connection.rollback()

            raise

    def close(self):

        self.database.close()