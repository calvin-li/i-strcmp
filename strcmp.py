import ImageMaker


def strcmp(candidate):
    # create image of string
    textImg = ImageMaker.svg_to_image(ImageMaker.text_to_svg(candidate))

    # attempt OCR

    # process results?

    return True
