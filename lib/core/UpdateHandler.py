import os
from lib.core.TextHandler import TextHandler


class UpdateHandler(object):

    def __init__(self, arguments, config):
        print(config)
        self.args = arguments
        self.config = config
        TextHandler().debug(self.args)

        if(not self.data_present()):
            self.build_git()
            self.build_modules()

        if(self.update_needed()):
            self.update_git()
            self.update_modules()

    def update_needed(self):
        # Check for 'update=True' in args
        if(self.args.update is True):
            return True

        # Check the date on the previous update.
        if(self.git_update_required()):
            return True

        if(self.modules_update_required()):
            return True

        return false

    def data_present(self):
        # Check if the git directory is present
        path = "~/{mooscan}/{git}".format(mooscan=self.config['mooscan_path'],
                                          git=self.config['git_path'])
        gitpath = os.path.expanduser(path)
        print("Checking if git directory is present")
        # Check if it's populated
        # Check if it's updated

    def git_update_required(self):
        return True

    def modules_update_required(self):
        return True

    def update_git(self):
        print("Update the local git repository")

    def update_modules(self):
        print("Update the modules and save into the database")

    def build_git(self):
        print("Build git")

    def build_modules(self):
        print("Build modules")
