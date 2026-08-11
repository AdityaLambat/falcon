from consumer.kafka_consumer import FalconKafkaConsumer


def main():

    consumer = FalconKafkaConsumer()

    consumer.consume()


if __name__ == "__main__":
    main()