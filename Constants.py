class Constants(object):
    @property
    def temp_folder(self):
        return "temp"

    @property
    def text_margins(self):
        return 3

    @property
    def default_font_size(self):
        return 140

    @property
    def default_scale_factor(self):
        return 4

    @property
    def default_start_x(self):
        return 3

    @property
    def default_start_y(self):
        return 1

    @property
    def forbidden_strings(self):
        return [
            "Google",
            "Gøøgle",
            "GooglePlex",
            "Gооgle",
            "Apple",
            "G\u2009oogle",
            "G\u200boogle",
            "G\u2009o\u2009o\u2009g\u2009l\u2009e",
            "G00gle"
        ]


global_constants: Constants = Constants()

