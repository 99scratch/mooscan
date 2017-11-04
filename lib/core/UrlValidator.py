import requests
import argparse
import re


class UrlValidator(argparse.Action):
    def __init__(self, option_strings, dest, nargs=None, **kwargs):

        if nargs is not None:
            raise ValueError("nargs is not allowed")
        super(UrlValidator, self).__init__(option_strings, dest, **kwargs)

    def __call__(self, parser, namespace, values, option_string=None):
        # print('%r %r %r' % (namespace, values, option_string))

        print("Validating URL: {url}".format(url=values))
        url = values

        # Validate the URL format.
        p = re.compile('^(http|https)://')
        if(not p.match(url)):
            parser.exit("URL {url} is invalid. Please make sure you "
                        "include http:// or https://".format(url=url))

        # See if we can hit the /login/index.php page, and /lib/db/install.xml
        # We only care about a 200, not their content here.
        pages = ['/login/index.php', '/lib/db/install.xml']
        found = 0
        for page in pages:
            testurl = url + page
            r = requests.get(testurl)
            # TODO: Set the User-Agent header as per config file
            if(r.status_code == 200):
                found += 1

            if(len(r.history)):
                # Did we get a 301?
                # Likely http to https rollup in place.
                # If so, we'll use that in the future
                if(r.history[0].status_code == 301 and "https://" in r.url):
                    print("HTTP to HTTPS roll up detected. "
                          "Enforcing HTTPS for all future requests")
                    p = re.compile('^http:')
                    updatedurl = p.sub('https:', url)
                    url = updatedurl

        if found == len(pages):
            print("URL {url} is Moodle".format(url=url))
            setattr(namespace, self.dest, url)
        else:
            parser.exit("URL {url} does not appear to be Moodle. "
                        "Did you forget a subdirectory?".format(url=url))
