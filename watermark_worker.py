import pika
import json
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
from constants import LOCALHOST, PILLOW_FONT
from pika_abstraction import (establish_connection, create_channel, declare_mq_queue,
                              basic_consume)


def save_watermark(input_image_path, output_image_path, text, x_position, y_position, r, g, b):
    photo = Image.open(input_image_path)  # open image from message
    drawing = ImageDraw.Draw(photo)  # creating a draw instance
    color = (r, g, b)  # creating tuple for color from message data
    font = ImageFont.truetype(PILLOW_FONT[0], PILLOW_FONT[1])  # setting up a font
    drawing.text((x_position, y_position), text, fill=color, font=font)  # drawing watermark
    photo.save(output_image_path)  # saving the image to the destination file system path from message


def process_watermarks(ch, method, properties, body):
    print(" [x] Received message: %r" % body)
    message = json.loads(body)  # deserializing message data
    save_watermark(**message)  # unpacking message data as arguments into the function


if __name__ == '__main__':
    connection = establish_connection(LOCALHOST)  # connecting to rabbitmq instance
    channel = create_channel(connection)  # creating a channel
    declare_mq_queue(channel, 'watermarks')  # declaring a queue
    basic_consume(channel, 'watermarks', process_watermarks, auto_ack=True)  # consuming from the queue
    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()  # starting a infinite process which consumes messages