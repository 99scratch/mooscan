from lib.core.UrlValidator import UrlValidator
from lib.core.__version__ import __version__

class ScanHandler():

    def __init__(self, arguments, config, db):
        self.args = arguments
        self.config = config
        self.db = db

        if self.args.url is None:
            print("No URL to scan provided. Nothing to do")
            return
        else:
            print("Scan of {url} requested. Initiating..."
                    .format(url=self.args.url))

        if self.args.themes is True or self.args.allscans is True:
            self.theme_scan()

        if self.args.mdlversion is True or self.args.allscans is True:
            self.version_scan()

        if self.args.plugin is True or self.args.allscans is True:
            self.plugin_scan()

        if self.args.vulns is True or self.args.allscans is True:
            self.vuln_scan()

        if self.args.public is True or self.args.allscans is True:
            self.public_scan()

    # get the URL we are scanning
    def get_target_url(self):
        if self.args.url is not None:
            return self.args.url

    def version_scan(self):
        print("Scan to determine remote Moodle version")

    def theme_scan(self):
        print("Scan for themes on the target")

    def plugin_scan(self):
        print("Scan for plugins on the target")

    def vuln_scan(self):
        print("Vuln scan of the target")

    def public_scan(self):
        print("Scan for files which may be leakind secrets")

