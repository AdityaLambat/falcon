import json

from confluent_kafka import Consumer

from config.kafka_config import (
    KAFKA_BOOTSTRAP_SERVERS,
    KAFKA_TOPIC,
    KAFKA_GROUP_ID
)

from services.event_processor import EventProcessor


class FalconKafkaConsumer:

    def __init__(self):

        self.consumer = Consumer({
            "bootstrap.servers": KAFKA_BOOTSTRAP_SERVERS,
            "group.id": KAFKA_GROUP_ID,
            "auto.offset.reset": "earliest",
            "enable.auto.commit": True
        })

        self.consumer.subscribe([KAFKA_TOPIC])

        self.event_processor = EventProcessor()

    def consume(self):

        try:

            while True:

                message = self.consumer.poll(1.0)

                if message is None:
                    continue

                if message.error():
                    continue

                event = json.loads(
                    message.value().decode("utf-8")
                )

                self.event_processor.process(event)

        except KeyboardInterrupt:

            pass

        finally:

            self.consumer.close()