from services.customer_ingestion import CustomerIngestion
from services.account_ingestion import AccountIngestion
from services.beneficiary_ingestion import BeneficiaryIngestion
from services.customer_device_ingestion import CustomerDeviceIngestion
from services.transaction_ingestion import TransactionIngestion


def main():

    customer_ingestion = CustomerIngestion()
    account_ingestion = AccountIngestion()
    beneficiary_ingestion = BeneficiaryIngestion()
    customer_device_ingestion = CustomerDeviceIngestion()
    transaction_ingestion = TransactionIngestion()

    customer_ingestion.ingest_csv(
        "csv/customer.csv"
    )

    account_ingestion.ingest_csv(
        "csv/account.csv"
    )

    beneficiary_ingestion.ingest_csv(
        "csv/beneficiary.csv"
    )

    customer_device_ingestion.ingest_csv(
        "csv/customer_device.csv"
    )

    transaction_ingestion.ingest_csv(
        "csv/transaction.csv"
    )


if __name__ == "__main__":
    main()