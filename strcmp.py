import ImageMaker
import Matcher


def strcmp(candidate, search_images, temp_folder):
    # create image of string
    text_img = ImageMaker.svg_to_image(ImageMaker.text_to_svg(candidate, temp_folder))

    # attempt OCR
    Matcher.match(text_img, search_images)

    # process results?

    return True
