#!/usr/bin/env python

import sys
from lib.core.__version__ import __version__
from lib.core.banner import banner
from lib.core.ConfigHandler import ConfigHandler
from lib.core.UpdateHandler import UpdateHandler
from lib.core.CliArgHandler import CliArgHandler
from lib.core.DatabaseHandler import DatabaseHandler


arguments = None


def main():
    print(banner(__version__).banner())

    startup_tasks()
    config = ConfigHandler()
    config.LoadConfig()
    loaded_config = config.GetLoadedConfig()

    arguments = CliArgHandler().parse(sys.argv[1:])

    db = DatabaseHandler(arguments, loaded_config)
    UpdateHandler(arguments, loaded_config, db)


def startup_tasks():
    print("Startup")

if __name__ == "__main__":
    main()
