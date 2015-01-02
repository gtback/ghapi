Use the GitHub API to get a list of all the open issues in a repository

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
