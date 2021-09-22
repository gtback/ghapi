# ghapi

A small GitHub API client in Python

## About

Use the GitHub API for a few common tasks:

- Get a list of all repositories in an organization.
- Get a list of all issues and PRs in a repository.
- Check for users who don't have 2FA enabled on an organization (that you own).

## Quick Start

Create a GitHub [personal access token](https://github.com/settings/tokens).

```shell
$ mkvirtualenv ghapi
$ git clone https://github.com/gtback/ghapi.git
$ cd ghapi
$ cat .ghcreds
gtback
<GitHub Personal Access Token>
$ ./ghapi issues gtback/ghapi
```

You can also set `GITHUB_USER` and `GITHUB_TOKEN` environment variables, rather
than using the `.ghcreds` file.
