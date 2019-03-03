import ImageMaker
import Matcher
import Ocr

threshold = 0.9


def strcmp(candidate, search_text, search_image, temp_folder):
    # create image of string
    text_img = ImageMaker.text_to_image(candidate, temp_folder, x_padding=10)

    # attempt OCR
    Ocr.ocr(search_text, search_image)
    return
