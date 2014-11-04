#!/usr/bin/env python
from ghapi import get_issues, print_issues

issues = get_issues("CybOXProject/schemas")

print_issues(issues, sort=True)
