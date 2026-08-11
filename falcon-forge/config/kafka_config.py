import os
from dotenv import load_dotenv


load_dotenv()


KAFKA_BOOTSTRAP_SERVERS = os.getenv("KAFKA_BOOTSTRAP_SERVERS")
KAFKA_TOPIC = os.getenv("KAFKA_TOPIC")

EVENT_TYPE_CUSTOMER = "falcon_Customer"
EVENT_TYPE_ACCOUNT = "falcon_Account"
EVENT_TYPE_BENEFICIARY = "falcon_Beneficiary"
EVENT_TYPE_CUSTOMER_DEVICE = "falcon_CustomerDevice"
EVENT_TYPE_TRANSACTION = "falcon_Transaction"


print(KAFKA_BOOTSTRAP_SERVERS)