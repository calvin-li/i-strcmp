import shutil

from ImageMaker import text_to_image
from Constants import global_constants as constants
from strcmp import strcmp
from datetime import datetime
import os


def main():
    if not os.path.exists(constants.temp_folder):
        os.mkdir(constants.temp_folder)
    temp_folder = constants.temp_folder + "/" + datetime.now().isoformat()
    if not os.path.exists(temp_folder):
        os.mkdir(temp_folder)
    forbidden_images = [text_to_image(s, temp_folder) for s in constants.forbidden_strings]
    test = strcmp("Google", forbidden_images, temp_folder)

    shutil.rmtree(temp_folder)
    return test


main()
