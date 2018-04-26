
class banner(object):
    def __init__(self, version):
        self.version = version

    def banner(self):
        banner = """
888b     d888                 .d8888b.
8888b   d8888                d88P  Y88b
88888b.d88888                Y88b.
888Y88888P888 .d88b.  .d88b.  "Y888b.   .d8888b 8888b. 88888b.
888 Y888P 888d88""88bd88""88b    "Y88b.d88P"       "88b888 "88b
888  Y8P  888888  888888  888      "888888     .d888888888  888
888   "   888Y88..88PY88..88PY88b  d88PY88b.   888  888888  888
888       888 "Y88P"  "Y88P"  "Y8888P"  "Y8888P"Y888888888  888

"""

        text = """MooScan - by @vortexau
Please do not use this tool against environments you do not have
 explicit permission to scan. The author will not be held responsible
 for any unauthorised usage of this software.
"""
        return banner + text
