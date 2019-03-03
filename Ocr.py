from PIL import Image
from pytesseract import pytesseract


def ocr(text, image_path):
    ocr_text = pytesseract.image_to_string(Image.open(image_path))
    print(ocr_text)
