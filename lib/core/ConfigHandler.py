import os
import yaml
import sys
from shutil import copyfile
from lib.core.TextHandler import TextHandler


class ConfigHandler(object):

    CONFIG_PATH = "~/.mooscan"
    CONFIG_FILE = "mooscan.conf"
    GIT_PATH = "moodle-git"

    def __init__(self):

        # Load the config paths
        self.LoadConfigPaths()

        # Path to the config
        self.CreateConfigDirectory()
        self.CreateConfig()

        self.config = self.LoadConfig()

    def LoadConfigPaths(self):

        if os.environ.get('MOOSCAN_CONFIG_PATH'):
            self.configdir = os.environ.get('MOOSCAN_CONFIG_PATH')
        else:
            self.configdir = os.path.expanduser(self.CONFIG_PATH)

        self.configfile = self.configdir + '/' + self.CONFIG_FILE

    def GetConfigFile(self):
        return self.configfile

    def CreateConfigDirectory(self):
        if not os.path.exists(self.configdir):
            TextHandler().debug("Configuration directory {dir} does not exist".
                                format(dir=self.configdir))
            os.makedirs(self.configdir)
            print("Directory Created")

    def CreateConfig(self):
        if not os.path.exists(self.configfile):
            copyfile('./doc/mooscan.conf.skel', self.configfile)
            TextHandler().debug("Config not found. Copying Default to {file}".
                                format(file=self.configfile))

    def LoadConfig(self):
        config = yaml.load(open(self.configfile, 'rb').read())
        checked = self.CheckConfig(config)
        return checked

    def CheckConfig(self, config):
        print("Validate the config here")
        return config
