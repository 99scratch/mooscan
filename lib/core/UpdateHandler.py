import os
from git import Repo
from lib.core.TextHandler import TextHandler


class UpdateHandler(object):

    def __init__(self, arguments, config):
        print(config)
        self.args = arguments
        self.config = config
        TextHandler().debug(self.args)

        if(self.update_needed()):
            self.update_git()

        # Iterate through each tagged branch in the git repo
        # and hash each file which is public.

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

    def update_git(self):

        # Check if the git directory is present
        path = "~/{mooscan}/{git}".format(mooscan=self.config['mooscan_path'],
                                          git=self.config['git_path'])
        gitpath = os.path.expanduser(path)

        if(os.path.exists(gitpath)):
            TextHandler().debug("Moodle code discovered at {dir}. "
                                "Getting latest."
                                .format(dir=gitpath))
            repo = Repo(gitpath)
            pull = repo.remotes.origin
            pull.pull()
            TextHandler().debug("Done")
            # Check the date of the last repo pull
        else:
            TextHandler().debug("Creating target git repository at {dir}"
                                .format(dir=gitpath))
            os.makedirs(gitpath)
            TextHandler().debug("Pulling the Moodle Git repo from {url}"
                                .format(url=self.config['moodle_git']))
            Repo.clone_from(self.config['moodle_git'], gitpath)
            TextHandler().debug("Done")
        # Check if it's updated

    def git_update_required(self):
        return True

    def modules_update_required(self):
        return True

    def update_modules(self):
        print("Update the modules and save into the database")

    def build_git(self):
        print("Build git")

    def build_modules(self):
        print("Build modules")
