import ImageMaker
import Matcher


def strcmp(candidate, search_images, temp_folder):
    # create image of string
    text_img = ImageMaker.text_to_image(candidate, temp_folder, x_padding=10)

    # attempt OCR
    Matcher.match(text_img, search_images)

    # process results?

    return True
