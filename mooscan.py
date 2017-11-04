#!/usr/bin/env python

import sys
from lib.core.__version__ import __version__
from lib.core.banner import banner
from lib.core.ConfigHandler import ConfigHandler
from lib.core.UpdateHandler import UpdateHandler
from lib.core.CliArgHandler import CliArgHandler


loaded_config = None
arguments = None


def main():
    print(banner(__version__).banner())

    startup_tasks()

    arguments = CliArgHandler(loaded_config).parse(sys.argv[1:])

    UpdateHandler(arguments, loaded_config)


def startup_tasks():
    loaded_config = ConfigHandler().LoadConfig()

if __name__ == "__main__":
    main()
