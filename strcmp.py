import ImageMaker
import Matcher


threshold = 0.9


def strcmp(candidate, search_text, search_image, temp_folder):
    # create image of string
    text_img = ImageMaker.text_to_image(candidate, temp_folder, x_padding=10)

    # attempt template matching
    results, score = Matcher.match(search_text, text_img, search_image)

    # process results?
    return score >= threshold
