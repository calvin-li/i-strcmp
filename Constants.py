class Constants(object):
    @property
    def temp_folder(self):
        return "temp"

    @property
    def text_margins(self):
        return 3

    @property
    def default_font_size(self):
        return 14


global_constants: Constants = Constants()

