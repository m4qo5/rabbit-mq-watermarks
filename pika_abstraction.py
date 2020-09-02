import pika


def establish_connection(host):
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(host=host)
    )
    return connection


def create_channel(connection):
    return connection.channel()


def declare_mq_queue(channel, queue_name):
    channel.queue_declare(queue=queue_name)


def basic_consume(channel, queue_name, callback_on_consume, auto_ack):
    channel.basic_consume(
        queue=queue_name,
        on_message_callback=callback_on_consume,
        auto_ack=auto_ack
    )


def publish_watermarks(channel, exchange, routing_key, body):
    channel.basic_publish(exchange=exchange,
                          routing_key=routing_key,
                          body=body)