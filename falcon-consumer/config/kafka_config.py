import os

from dotenv import load_dotenv


load_dotenv()


KAFKA_BOOTSTRAP_SERVERS = os.getenv(
    "KAFKA_BOOTSTRAP_SERVERS"
)

KAFKA_TOPIC = os.getenv(
    "KAFKA_TOPIC"
)

KAFKA_GROUP_ID = os.getenv(
    "KAFKA_GROUP_ID",
    "falcon-consumer"
)