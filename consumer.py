
import os
import time

from confluent_kafka import Consumer


if __name__ == "__main__":
    time.sleep(60)

    consumer_conf = {
        "bootstrap.servers": os.getenv("KAFKA_BOOTSTRAP_SERVERS"),
        "group.id": os.getenv("KAFKA_GROUP_ID"),
        "auto.offset.reset": "earliest",

        "security.protocol": "SASL_SSL",
        "ssl.ca.location": "ca.crt",
        "ssl.certificate.location": "kafka-0-creds/kafka-0.crt",
        "ssl.key.location": "kafka-0-creds/kafka-0.key",

        "ssl.endpoint.identification.algorithm": "none",
        "sasl.mechanism": "PLAIN",
        "sasl.username": os.getenv("SASL_USERNAME"),
        "sasl.password": os.getenv("SASL_PASSWORD"),
    }

    try:
        consumer = Consumer(consumer_conf)
        consumer.subscribe(["topic-1", "topic-2"])

        try:
            while True:
                message = consumer.poll(1)

                if message is None:
                    continue
                if message.error():
                    print(f"Ошибка при получении сообщения: {message.error()}")
                    continue

                key = message.key().decode("utf-8")
                value = message.value().decode("utf-8")
                offset = message.offset()
                print(f"Получено сообщение: key='{key}', value='{value}', {offset=}")
        finally:
            consumer.close()
    except Exception as e:
        print(e)