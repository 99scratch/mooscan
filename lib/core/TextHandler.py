
class TextHandler(object):

    # This doesn't do too much as yet.
    # The idea is that down the track we can add colours as needed
    # to draw attention to certin types of errors, warnings etc.

    def info(self, text):
        print("[I] {text}".format(text=text))

    def emerg(self, text):
        print("[EM] {text}".format(text=text))

    def error(self, text):
        print("[E] {text}".format(text=text))

    def warning(self, text):
        print("[W] {text}".format(text=text))

    def debug(self, text):
        print("[D] {text}".format(text=text))
