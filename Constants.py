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

    @property
    def default_scale_factor(self):
        return 4

    @property
    def forbidden_strings(self):
        return ["Google", "Gооgle", "Apple"]


global_constants: Constants = Constants()

