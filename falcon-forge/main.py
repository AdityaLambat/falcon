from datetime import UTC, datetime

from producer.kafka_producer import FalconKafkaProducer
from config.kafka_config import EVENT_TYPE

producer = FalconKafkaProducer()

event = {
    "eventType": EVENT_TYPE,
    "eventVersion": "1.0",
    "eventTimestamp": datetime.now(UTC).isoformat(),
    "payload": {
        "transactionReferenceNumber": "TXN000001",
        "amount": 1000,
        "currency": "INR"
    }
}

producer.publish(event)