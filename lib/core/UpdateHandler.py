import os
import subprocess
import time
from git import Repo
from lib.core.TextHandler import TextHandler
from lib.core.DatabaseHandler import DatabaseHandler


class UpdateHandler(object):

    def __init__(self, arguments, config, db):
        print(config)
        self.args = arguments
        self.config = config
        self.db = db

        self.build_git_path()

        if(self.git_update_required() or self.args.update is True):
            self.update_git()

        if(self.modules_update_required() or self.args.update is True):
            self.update_modules()

    def build_git_path(self):

        # Check if the git directory is present
        if os.environ.get('MOOSCAN_DATA_PATH'):
            TextHandler().debug("Environment variable MOOSCAN_DATA_PATH is "
                                "set, ignoring config value")
            mooscan = os.environ.get('MOOSCAN_DATA_PATH')
        else:
            mooscan = self.config['mooscan_path']

        path = "{mooscan}/{git}".format(mooscan=mooscan,
                                        git=self.config['git_path'])

        self.gitpath = os.path.expanduser(path)

    def update_git(self):

        self.db.create_code_db()

        if(os.path.exists(self.gitpath)):
            TextHandler().debug("Moodle code discovered at {dir}. "
                                "Getting latest."
                                .format(dir=self.gitpath))
            repo = Repo(self.gitpath)
            pull = repo.remotes.origin
            pull.pull()
            TextHandler().debug("Done")
        else:
            TextHandler().debug("Creating target git repository at {dir}"
                                .format(dir=self.gitpath))
            os.makedirs(self.gitpath)
            TextHandler().debug("Pulling the Moodle Git repo from {url}"
                                .format(url=self.config['moodle_git']))
            Repo.clone_from(self.config['moodle_git'], self.gitpath)
            TextHandler().debug("Done")

    def git_update_required(self):
        checkfile = "{gitpath}/.git/FETCH_HEAD".format(gitpath=self.gitpath)

        if not os.path.isfile(checkfile):
            return True

        lastchange = subprocess.run(['stat',
                                     '-c',
                                     '%Y',
                                     checkfile
                                     ], stdout=subprocess.PIPE)
        timestamp = int(lastchange.stdout.strip())

        exp = time.time() + (self.config['update_code_freq'] * 86400)

        if(int(exp) < int(timestamp)):
            return True
        else:
            return False

    def modules_update_required(self):
        return True

    def update_modules(self):
        TextHandler().debug("Update the modules and save into the database")
        TextHandler().debug("Done")

    def build_git(self):
        print("Build git")

    def build_modules(self):
        print("Build modules")
