from PIL import ImageDraw, Image, ImageFont

from Constants import global_constants as constants
from find_text_dimensions import find_text_dimensions


def default_font_string(weight, family):
    return "\n\t{{ font: {0} {1}px {2}; }}\n".format(weight, constants.default_font_size, family)


def get_image_name(input_text, temp_folder):
    return "{0}/{1}.png".format(
        temp_folder, str(abs(hash(input_text)) % (10 ** 8)))


def text_to_image(text, temp_folder, x_padding=0):
    text_width, text_height = find_text_dimensions(text, constants.default_font_size)
    x_padding += constants.text_margins
    width = text_width + 2 * x_padding
    height = text_height + 2 * constants.text_margins
    image = Image.new('L', (int(width), int(height)), 256)
    draw = ImageDraw.Draw(image)
    draw.text(
        (constants.default_start_x + x_padding / 2, constants.default_start_y),
        text,
        font=ImageFont.truetype("Arial.ttf", constants.default_font_size))
    image_path = get_image_name(text, temp_folder)
    image.save(image_path, "png")
    return image_path
