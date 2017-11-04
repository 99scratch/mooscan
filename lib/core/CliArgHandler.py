from argparse import ArgumentParser
from lib.core.UrlValidator import UrlValidator
from lib.core.__version__ import __version__


class CliArgHandler(object):
    def __init__(self, config):
        self._parser = self.setup_cli_parser()
        self.config = config

    def parse(self, argv):
        return self._parser.parse_args(argv)

    @staticmethod
    def setup_cli_parser():
        parser = ArgumentParser()

        parser.add_argument(
            '--url',
            action=UrlValidator,
            help='Moodle Host to scan Ex: '
                 'https://www.mymoodle.com. Use full path if required'
        )

        parser.add_argument(
            '-u',
            '--update',
            action='store_true',
            help='Start update of the tool. This may take a while, '
                 'perhaps go to lunch now.'
        )

        parser.add_argument(
            '-a',
            '--allscans',
            action='store_true',
            default=True,
            help='Run all possible scans. This is enabled by default'
        )

        parser.add_argument(
            '-ht',
            '--htaccess',
            action='store_true',
            help='Generate .htaccess file to prevent access to '
                 'discovered files'
        )

        parser.add_argument(
            '-v',
            '--verbose',
            action='count',
            help='Use Verbose mode'
        )

        parser.add_argument(
            '-V',
            '--version',
            action='version',
            version=__version__,
            help='Version of mooscan'
        )

        return parser
