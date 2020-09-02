import pika
import json
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
from constants import LOCALHOST, PILLOW_FONT
from pika_abstraction import (establish_connection, create_channel, declare_mq_queue,
                              basic_consume)


def save_watermark(input_image_path, output_image_path, text, x_position, y_position, r, g, b):
    photo = Image.open(input_image_path)
    drawing = ImageDraw.Draw(photo)
    color = (r, g, b)
    font = ImageFont.truetype(PILLOW_FONT[0], PILLOW_FONT[1])
    drawing.text((x_position, y_position), text, fill=color, font=font)
    photo.save(output_image_path)


def process_watermarks(ch, method, properties, body):
    print(" [x] Received message: %r" % body)
    message = json.loads(body)
    save_watermark(**message)


if __name__ == '__main__':
    connection = establish_connection(LOCALHOST)
    channel = create_channel(connection)
    declare_mq_queue(channel, 'watermarks')
    basic_consume(channel, 'watermarks', process_watermarks, auto_ack=True)
    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()