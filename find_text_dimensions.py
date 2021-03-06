import cairo
import Constants


# Source: http://blog.mathieu-leplatre.info/text-extents-with-python-cairo.html
def find_text_dimensions(text, font_size):
    surface = cairo.SVGSurface('undefined.svg', 1280, 200)
    cr = cairo.Context(surface)
    cr.select_font_face('Arial', cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_BOLD)
    cr.set_font_size(font_size)
    _, _, width, height, _, _ = cr.text_extents(text)
    return width, height*Constants.global_constants.default_font_size/100.0
