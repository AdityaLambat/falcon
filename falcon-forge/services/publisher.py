from producer.kafka_producer import FalconKafkaProducer


class Publisher:

    def __init__(self):
        self.producer = FalconKafkaProducer()

    def publish(self, event):

        return self.producer.publish(event.to_dict())