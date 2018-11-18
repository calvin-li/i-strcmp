import xml.etree.ElementTree as eTree
from datetime import datetime

from reportlab.graphics import renderPM
from svglib import svglib

from Constants import global_constants as constants
from find_text_dimensions import find_text_dimensions


def default_font_string(weight, family):
    return "\n\t{{ font: {0} {1}px {2}; }}\n".format(weight, constants.default_font_size, family)


def text_to_svg(input_text, font_string="", weight="regular", family="sans-serif"):
    style_tag = '{http://www.w3.org/2000/svg}'
    svg = eTree.parse("template.svg")
    svg_root = svg.getroot()

    if font_string == "":
        font_string = default_font_string(weight, family)
    text_width, text_height = find_text_dimensions(input_text, constants.default_font_size)

    width = text_width + 2 * constants.text_margins
    height = text_height + 2 * constants.text_margins
    svg_root.attrib["width"] = str(width) + "px"
    svg_root.attrib["height"] = str(height) + "px"

    svg_style = svg_root.find(style_tag + "style")
    svg_style.text = font_string

    svg_text = svg_root.find(style_tag + "text")
    svg_text.text = input_text
    svg_text.attrib["x"] = str(constants.text_margins) + "px"
    svg_text.attrib["y"] = str(text_height) + "px"

    svg_name = "{0}/generated.{1}.svg".format(
        constants.temp_folder, datetime.now().isoformat())
    svg.write(svg_name)
    return svg_name


def svg_to_image(svg, scale_factor=4):
    png = svglib.svg2rlg(svg)
    png.scale(scale_factor, scale_factor)
    png_path = svg.replace(".svg", ".png")

    renderPM.drawToFile(png, png_path, fmt="PNG", dpi=72*scale_factor)
    return png_path


def text_to_image(text):
    return svg_to_image(text_to_svg(text))
