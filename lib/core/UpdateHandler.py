from lib.core.TextHandler import TextHandler


class UpdateHandler(object):

    def __init__(self, arguments, config):
        self.args = arguments
        self.config = config
        TextHandler().debug(self.args)

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

    def git_update_required(self):
        return True

    def modules_update_required(self):
        return True

    def update_git(self):
        print("Update the local git repository")

    def update_modules(self):
        print("Update the modules and save into the database")
