LOCALHOST = 'localhost'
PILLOW_FONT = ('Pillow/Tests/fonts/FreeMono.ttf', 40)  # watermark font
WATERMARKS_QUEUE = 'watermarks'  # queue name
INPUT_IMAGE = './images/image.jpg'  # default image path
OUTPUT_IMAGE = './watermarks/image.jpg'  # default destination image path

MESSAGE_EXAMPLE = {
    'input_image_path' : INPUT_IMAGE,
    'output_image_path' : OUTPUT_IMAGE,
    'text' : 'Some text for watermark',
    'x_position' : 0,
    'y_position' : 0,
    'r' : 0,
    'g' : 0,
    'b' : 0,
}