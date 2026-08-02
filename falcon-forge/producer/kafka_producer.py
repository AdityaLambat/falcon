import json
from confluent_kafka import Producer

from config.kafka_config import (
    KAFKA_BOOTSTRAP_SERVERS,
    KAFKA_TOPIC
)


class FalconKafkaProducer:

    def __init__(self):
        self.producer = Producer({
            "bootstrap.servers": KAFKA_BOOTSTRAP_SERVERS
        })

    @staticmethod
    def delivery_report(err, msg):
        if err is not None:
            print(f"❌ Message delivery failed: {err}")
        else:
            print("✅ Event published successfully.")
            print(f"Topic     : {msg.topic()}")
            print(f"Partition : {msg.partition()}")
            print(f"Offset    : {msg.offset()}")

    def publish(self, event):

        self.producer.produce(
            topic=KAFKA_TOPIC,
            value=json.dumps(event),
            callback=self.delivery_report
        )

        self.producer.flush()