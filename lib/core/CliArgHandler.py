from argparse import ArgumentParser

class CliArgHandler(object):
    def __init__(self):
        self._parser = self.setup_cli_parser()

    def parse(self, argv):
        return self._parser.parse_args(argv)

    @staticmethod
    def setup_cli_parser():
        parser = ArgumentParser()

        update = parser.add_mutually_exclusive_group()
        update.add_argument(
            '-u', '--url',
            dest='url',
            help='Moodle Host to scan Ex: '
                 'https://www.mymoodle.com. Use full path if required'
        )

        update.add_argument(
            '-up','--update',
            dest='update',
            help='Start update of the tool. This may take a while, perhaps go to lunch now.'
        )

        parser.add_argument(
            '-a','--allscans',
            dest='allscans',
            default=True,
            help='Run all possible scans. This is enabled by default'
        )

        parser.add_argument(
            '-ht', '--htaccess',
            dest='htaccess',
            help='Generate .htaccess file to prevent access to discovered files'
        )

        parser.add_argument(
            '-v','--verbose',
            dest='verbose',
            choices=[0,1,2,3],
            help='Use Verbose mode'
        )

        parser.add_argument(
            '-V','--version',
            dest='version',
            help='Version of mooscan'
        )

        return parser
