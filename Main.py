from Constants import global_constants as constants
from strcmp import strcmp
import os


def main():
    if not os.path.exists(constants.temp_folder):
        os.mkdir(constants.temp_folder)
    test = strcmp("Google")
    return test


main()
