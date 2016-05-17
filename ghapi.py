import csv
from datetime import datetime
import json
import logging
from StringIO import StringIO

import requests


logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


with open(".ghcreds") as f:
    USERNAME, APIKEY = [x.strip() for x in f.readlines()]


def get_issue_from_file(filename):
    with open(filename) as f:
        issues = json.load(f)


def write_issues_csv(issue_list, filename):
    s = StringIO()
    sw = csv.writer(s)

    for issue in sorted(issues, key=lambda x:int(x['number'])):
        i = Issue(issue)
        sw.writerow([i.number, i.title, i.milestone, i.priority, i.actions_str])

    with open(filename, "wt") as f2:
        f2.write(s.getvalue())


def get_links(r):
    links = {}

    if 'link' in r.headers:
        for link in r.headers['link'].split(','):
            url, rel = link.split(';')
            url = url.strip().strip('<>')
            rel = rel.split('"')[1]
            links[rel] = url

    return links


def call_api(url):
    authorization = 'token {}'.format(APIKEY)
    user_agent = USERNAME + " python-requests/" + requests.__version__
    headers = {'Authorization': authorization, 'User-Agent': user_agent}

    response = requests.get(url, headers=headers)

    if response.status_code != requests.codes.ok:
        raise ValueError("API Error: %s" % response.json()['message'])

    return response


def _unpaginate(url):
    """Repeatedly call an API until there is no 'next' parameter.

    The URL should should return JSON consisting of a list of items.
    """

    items = []

    while url:
        r = call_api(url)
        url = get_links(r).get('next')

        items.extend(r.json())

    return items


def get_issues(repo):
    issues = []

    url = "https://api.github.com/repos/%s/issues" % repo
    issues = _unpaginate(url)

    return issues


def print_issues(issues, sort=False):
    if sort:
        issues = sorted(issues, key=lambda x:int(x['number']))

    for issue in issues:
        i = Issue(issue)
        fields =  [i.number, i.title, i.url, ",".join(i.labels)]
        print "\t".join(str(x) for x in fields)


def ratelimit_info(response):
    print response.headers["X-RateLimit-Limit"]
    print response.headers["X-RateLimit-Remaining"]
    reset_date = float(response.headers["X-RateLimit-Reset"])
    print datetime.fromtimestamp(reset_date).isoformat()


class Issue(object):

    def __init__(self, d):
        self._d = d

    @property
    def number(self):
        return self._d['number']

    @property
    def title(self):
        return self._d['title']

    @property
    def url(self):
        return self._d['html_url']

    @property
    def milestone(self):
        if not self._d['milestone']:
            return None
        return self._d['milestone']['title']

    @property
    def labels(self):
        return [lbl['name'] for lbl in self._d['labels']]

    @property
    def priority(self):
        for l in self.labels:
            if l.startswith("Pri"):
                return l
        return None

    @property
    def actions(self):
        return [str(l) for l in self.labels if l in
                ('New Type', 'Expand Type', 'Modify Type', 'Documentation')]

    @property
    def actions_str(self):
        return ", ".join(i.actions) if i.actions else ""

    def as_dict(self):
        pprint(self._)


def tfa_users(org):
    url = "https://api.github.com/orgs/%s/members?filter=2fa_disabled" % org

    users = _unpaginate(url)
    for user in users:
        print user['login']
