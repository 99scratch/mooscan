#!/usr/bin/env python

import sys
from lib.core.__version__ import __version__
from lib.core.banner import banner
from lib.core.ConfigHandler import ConfigHandler
from lib.core.CliArgHandler import CliArgHandler


def main():
    print(banner(__version__).banner())

    parser = CliArgHandler()
    arguments = parser.parse(sys.argv[1:])

    print(arguments)

    startup_tasks()


def startup_tasks():
    ConfigHandler()

if __name__ == "__main__":
    main()
