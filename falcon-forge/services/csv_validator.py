from decimal import Decimal

from models.enums.channel import Channel
from models.enums.transaction_status import TransactionStatus
from models.enums.transaction_type import TransactionType
from models.enums.kyc_status import KycStatus
from models.enums.customer_status import CustomerStatus
from models.enums.risk_category import RiskCategory
from models.enums.account_type import AccountType
from models.enums.account_status import AccountStatus
from models.enums.beneficiary_status import BeneficiaryStatus
from models.enums.device_status import DeviceStatus


class CsvValidator:

    CUSTOMER_REQUIRED_FIELDS = [
        "customerId",
        "firstName",
        "lastName",
        "dateOfBirth",
        "mobileNumber",
        "email",
        "address",
        "city",
        "state",
        "country",
        "kycStatus",
        "customerStatus",
        "riskCategory"
    ]

    ACCOUNT_REQUIRED_FIELDS = [
        "accountId",
        "customerId",
        "accountNumber",
        "accountType",
        "branchCode",
        "ifscCode",
        "accountStatus",
        "balance",
        "openingDate",
        "lastTransactionDate"
    ]

    BENEFICIARY_REQUIRED_FIELDS = [
        "beneficiaryId",
        "accountId",
        "beneficiaryName",
        "beneficiaryAccountNumber",
        "beneficiaryBankName",
        "beneficiaryIfscCode",
        "beneficiaryStatus"
    ]

    CUSTOMER_DEVICE_REQUIRED_FIELDS = [
        "customerId",
        "deviceIdentifier",
        "lastSeenAt",
        "deviceStatus"
    ]

    TRANSACTION_REQUIRED_FIELDS = [
        "accountId",
        "beneficiaryId",
        "deviceIdentifier",
        "transactionReference",
        "channel",
        "transactionType",
        "amount",
        "transactionStatus"
    ]

    @staticmethod
    def validate(data: dict, entity_type: str = "transaction"):

        if entity_type == "customer":
            CsvValidator._validate_customer(data)

        elif entity_type == "account":
            CsvValidator._validate_account(data)

        elif entity_type == "beneficiary":
            CsvValidator._validate_beneficiary(data)

        elif entity_type == "customer_device":
            CsvValidator._validate_customer_device(data)

        elif entity_type == "transaction":
            CsvValidator._validate_transaction(data)

        else:
            raise ValueError(
                f"Unsupported entity type: {entity_type}"
            )

    # ---------------------------------------------------------
    # TRANSACTION
    # ---------------------------------------------------------

    @staticmethod
    def _validate_transaction(data: dict):

        CsvValidator._validate_required_fields(
            data,
            CsvValidator.TRANSACTION_REQUIRED_FIELDS
        )

        CsvValidator._validate_amount(data)
        CsvValidator._validate_channel(data)
        CsvValidator._validate_transaction_type(data)
        CsvValidator._validate_transaction_status(data)

    # ---------------------------------------------------------
    # CUSTOMER
    # ---------------------------------------------------------

    @staticmethod
    def _validate_customer(data: dict):

        CsvValidator._validate_required_fields(
            data,
            CsvValidator.CUSTOMER_REQUIRED_FIELDS
        )

        CsvValidator._validate_enum(
            data["kycStatus"],
            KycStatus,
            "kycStatus"
        )

        CsvValidator._validate_enum(
            data["customerStatus"],
            CustomerStatus,
            "customerStatus"
        )

        CsvValidator._validate_enum(
            data["riskCategory"],
            RiskCategory,
            "riskCategory"
        )

    # ---------------------------------------------------------
    # ACCOUNT
    # ---------------------------------------------------------

    @staticmethod
    def _validate_account(data: dict):

        CsvValidator._validate_required_fields(
            data,
            CsvValidator.ACCOUNT_REQUIRED_FIELDS
        )

        CsvValidator._validate_decimal(
            data["balance"],
            "balance"
        )

        CsvValidator._validate_enum(
            data["accountType"],
            AccountType,
            "accountType"
        )

        CsvValidator._validate_enum(
            data["accountStatus"],
            AccountStatus,
            "accountStatus"
        )

    # ---------------------------------------------------------
    # BENEFICIARY
    # ---------------------------------------------------------

    @staticmethod
    def _validate_beneficiary(data: dict):

        CsvValidator._validate_required_fields(
            data,
            CsvValidator.BENEFICIARY_REQUIRED_FIELDS
        )

        CsvValidator._validate_enum(
            data["beneficiaryStatus"],
            BeneficiaryStatus,
            "beneficiaryStatus"
        )

    # ---------------------------------------------------------
    # CUSTOMER DEVICE
    # ---------------------------------------------------------

    @staticmethod
    def _validate_customer_device(data: dict):

        CsvValidator._validate_required_fields(
            data,
            CsvValidator.CUSTOMER_DEVICE_REQUIRED_FIELDS
        )

        CsvValidator._validate_enum(
            data["deviceStatus"],
            DeviceStatus,
            "deviceStatus"
        )

    # ---------------------------------------------------------
    # COMMON VALIDATION
    # ---------------------------------------------------------

    @staticmethod
    def _validate_required_fields(data: dict, required_fields: list):

        for field in required_fields:

            if field not in data or not data[field]:

                raise ValueError(
                    f"{field} is mandatory."
                )

    @staticmethod
    def _validate_amount(data: dict):

        CsvValidator._validate_decimal(
            data["amount"],
            "amount"
        )

    @staticmethod
    def _validate_decimal(value, field_name: str):

        try:
            Decimal(value)

        except Exception:

            raise ValueError(
                f"Invalid {field_name}."
            )

    @staticmethod
    def _validate_channel(data: dict):

        CsvValidator._validate_enum(
            data["channel"],
            Channel,
            "channel"
        )

    @staticmethod
    def _validate_transaction_type(data: dict):

        CsvValidator._validate_enum(
            data["transactionType"],
            TransactionType,
            "transactionType"
        )

    @staticmethod
    def _validate_transaction_status(data: dict):

        CsvValidator._validate_enum(
            data["transactionStatus"],
            TransactionStatus,
            "transactionStatus"
        )

    @staticmethod
    def _validate_enum(value, enum_class, field_name: str):

        try:

            enum_class(value)

        except ValueError:

            raise ValueError(
                f"Invalid {field_name}: {value}"
            )