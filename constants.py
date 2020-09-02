LOCALHOST = 'localhost'
PILLOW_FONT = ('Pillow/Tests/fonts/FreeMono.ttf', 40)
WATERMARKS_QUEUE = 'watermarks'
INPUT_IMAGE = './images/image.jpg'
OUTPUT_IMAGE = './watermarks/image.jpg'

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