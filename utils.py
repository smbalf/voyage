from ctypes import windll, create_unicode_buffer


class Utilities:

    @classmethod
    def app_is_open(cls, game_name):
        window_name = windll.user32.GetForegroundWindow()
        length = windll.user32.GetWindowTextLengthW(window_name)
        application = create_unicode_buffer(length + 1)
        windll.user32.GetWindowTextW(window_name, application, length + 1)

        return application.value == game_name