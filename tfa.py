#!/usr/bin/env python

"""
Example:
    python tfs.py django
"""

import sys

from ghapi import tfa_users

tfa_users(sys.argv[1])


