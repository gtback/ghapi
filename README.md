Use the GitHub API for a few common tasks:
- get a list of all the open issues in a repository.
- check for users who don't have 2FA enabled on an organzation (that you own).

## Quickstart

```
$ mkvirtualenv ghapi
$ git clone https://github.com/gtback/ghapi.git
$ cd ghapi
$ cat .ghcreds
gtback
<GitHub Personal Access Token>
$ python issues.py gtback/ghapi
```

Create your Personal Access Token at
https://github.com/settings/applications#personal-access-tokens
