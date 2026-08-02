import json
from confluent_kafka import Producer

from config.kafka_config import (
    KAFKA_BOOTSTRAP_SERVERS,
    KAFKA_TOPIC
)


class FalconKafkaProducer:

    def __init__(self):

        self.metadata = None

        self.producer = Producer({
            "bootstrap.servers": KAFKA_BOOTSTRAP_SERVERS
        })

    def delivery_report(self, err, msg):

        if err is not None:
            raise Exception(f"Message delivery failed: {err}")

        self.metadata = {
            "topic": msg.topic(),
            "partition": msg.partition(),
            "offset": msg.offset()
        }

        print("✅ Event published successfully.")
        print(f"Topic     : {msg.topic()}")
        print(f"Partition : {msg.partition()}")
        print(f"Offset    : {msg.offset()}")

    def publish(self, event):

        self.metadata = None

        self.producer.produce(
            topic=KAFKA_TOPIC,
            value=json.dumps(event),
            callback=self.delivery_report
        )

        self.producer.flush()

        return self.metadata