import os
from dotenv import load_dotenv

load_dotenv()

KAFKA_BOOTSTRAP_SERVERS = os.getenv("KAFKA_BOOTSTRAP_SERVERS")
KAFKA_TOPIC = os.getenv("KAFKA_TOPIC")
EVENT_TYPE = os.getenv("EVENT_TYPE")
print(KAFKA_BOOTSTRAP_SERVERS)