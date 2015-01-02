#!/usr/bin/env python

"""
Example:
    python issues.py gtback/ghapi
"""

import sys

from ghapi import get_issues, print_issues

issues = get_issues(sys.argv[1])

print_issues(issues, sort=True)
