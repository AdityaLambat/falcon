from services.transaction_ingestion import TransactionIngestion


def main():

    ingestion = TransactionIngestion()

    ingestion.ingest_csv("csv/transactions.csv")


if __name__ == "__main__":
    main()