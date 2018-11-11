import xml.etree.ElementTree as eTree
from datetime import datetime
from cairosvg import svg2png


def text_to_svg(input_text):
    style_tag = '{http://www.w3.org/2000/svg}'
    svg = eTree.parse("template.svg")
    svg_text = svg.getroot().find(style_tag + "text")
    svg_text.text = input_text
    svg_name = "temp/generated." + datetime.now().isoformat() + ".svg"
    svg.write(svg_name)
    return svg_name


def svg_to_image(svg):
    png = svg.replace(".svg", ".png")
    svg2png(url=svg, write_to=png)
    return png


def text_to_image(text):
    return svg_to_image(text_to_svg(text))
