import pika
import json
from constants import LOCALHOST, WATERMARKS_QUEUE, INPUT_IMAGE, OUTPUT_IMAGE, MESSAGE_EXAMPLE
from pika_abstraction import (establish_connection, create_channel, declare_mq_queue,
                              basic_consume, publish_watermarks)


def setup_rabbit():
    connection = establish_connection(LOCALHOST)  # connecting to rabbitmq instance
    channel = create_channel(connection)  # creating a channel
    declare_mq_queue(channel, WATERMARKS_QUEUE)  # declaring a queue
    return connection, channel


def produce_message(channel, exchange):
    publish_watermarks(
        channel=channel, exchange=exchange,  # publishing a message to the queue
        routing_key=WATERMARKS_QUEUE,
        body=json.dumps(MESSAGE_EXAMPLE)
    )


if __name__ == '__main__':
    connection, channel = setup_rabbit()
    print(" [x] Connection to RabbitMQ established. You can save messages now")
    produce_message(channel, '')  # producing a message to the queue using default exchange
    print(" [x] Message with info about image has been produced")
