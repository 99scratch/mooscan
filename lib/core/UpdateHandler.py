import os
import subprocess
import time
import json
import requests
import glob
import re
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
        else:
            TextHandler().debug("No update required for Moodle code")

        if(self.modules_update_required() or self.args.update is True):
            self.update_modules()
        else:
            TextHandler().debug("No update required for Moodle plugins")

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

        if(os.path.exists(self.gitpath)):
            TextHandler().debug("Moodle code discovered at {dir}. "
                    "Getting latest."
                    .format(dir=self.gitpath))
            repo = Repo(self.gitpath)
            repo.git.checkout('master', force=True)
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

        self.git_parse_repo()

        self.db.save_updates('code')

    def git_parse_repo(self):
        # Loop through all tagged versions of Moodle in the git repo
        # This is honestly pretty bad. But until I decide to do this
        # "in the cloud" and offer a service for clients to update from
        # with this pre-parsed, it'll have to do...

        moodlegit = Repo(self.gitpath)
        tags = moodlegit.tags

        for tag in tags:
            if re.match('^v1.[0-6]', tag.name):
                print(tag.name)
                # unset the item from the list
                tags.remove(tag)

        TextHandler().info("Processing Moodle tagged versions...")
        for tag in tags:
            moodlegit.git.checkout(tag.name, force=True)

            # Nothing of interest is in Moodle before 1.7..

            print("Tag: {tag}".format(tag=tag.name), end='')

            # If there is no lib/db/install.xml, we don't care. It's too old.
            # You'll have to go old-school..
            if not os.path.exists(self.gitpath + '/lib/db/install.xml'):
                print("\r", end='')
                continue

            globpath = "{path}/**/*".format(path=self.gitpath)
            for strmdlfile in glob.glob(globpath, recursive=True):
                print(strmdlfile, flush=True)
                # Hash the file content itself
                strmdlfile = os.path.normpath(self.gitpath + "/" + str(mdlfile.decode()))

                if os.path.isdir(strmdlfile):
                    continue

                ignore = ['.php','.gif','.png','.jpg','.git']
                if strmdlfile in ignore:
                    continue

                filehash = hashlib.md5()
                try:
                    with open(strmdlfile, "rb") as f:
                        for chunk in iter(lambda: f.read(BUF), b""):
                            filehash.update(chunk)

                    print(strmdlfile + " MD5: " + filehash.hexdigest())

                    # If the file is 'install.xml' parse it, pull out the version number, save that too.
                    if 'install.xml' in strmdlfile:
                        print("**install.xml found** : {file}".format(file=strmdlfile))
                except:
                    print("FNF {file}".format(file=strmdlfile))  

    def git_update_required(self):
        updatedata = self.db.get_updates()

        if not updatedata:
            return True

        lastupdate = json.loads(updatedata.updates)

        if lastupdate.get('code') is None:
            return True

        timestamp = int(lastupdate['code'])

        exp = time.time() + (self.config['update_code_freq'] * 86400)

        if(int(exp) < int(timestamp)):
            return True
        else:
            return False

    def modules_update_required(self):
        updatedata = self.db.get_updates()

        if not updatedata:
            return True

        lastupdate = json.loads(updatedata.updates)

        if lastupdate.get('modules') is None:
            return True

        timestamp = int(lastupdate['modules'])
        exp = time.time() + (self.config['update_module_freq'] * 86400)

        if(int(exp) < int(timestamp)):
            return True
        else:
            return False

    def update_query(self, batch):
        outer = []
        inner = {}
        args = {}
        args['query'] = 'sort-by:publish'
        args['batch'] = batch

        inner['index'] = '0'
        inner['methodname'] = 'local_plugins_get_plugins_batch'
        inner['args'] = args

        outer.append(inner)

        return json.dumps(outer)

    def update_modules(self):
        TextHandler().debug("Update the modules and save into the database")

        # For testing we'll only pull 1 batch
        plugins = 1500  # Will need to automate this
        batches = plugins / 30
        for batch in range(0, int(batches)):

            print("Downloading: {batch}/{total}".format(
                batch=(batch * 30),
                total=plugins
                ),
                flush=True,
                end="\r"
                )

            query = self.update_query(batch)

            headers = {
                    'User-Agent': self.config['user_agent'],
                    'Content-Type': 'application/json',
                    'Content-Length': len(query)
                    }

            url = 'https://moodle.org/lib/ajax/service.php'

            request = requests.get(url, headers=headers, data=query)
            jsondata = request.json()
            resultset = jsondata[0]["data"]["grid"]["plugins"]

            # Parse each result
            for entry in resultset:

                # There is the concept of 'other' non-plugin
                # modules now. We're skipping them for now..
                # Example: https://moodle.org/plugins/view.php?id=1963
                if entry['plugintype']['type'] == '_other_':
                    continue

                self.db.save_module(entry)

        self.db.save_updates('modules')

        TextHandler().debug("Done")
