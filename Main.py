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
    test = [strcmp(
        "Google",
        constants.forbidden_strings[i],
        forbidden_images[i],
        temp_folder)
        for i in range(0, len(forbidden_images))]

    # shutil.rmtree(temp_folder)
    print(test)
    return test


main()
