#!/usr/bin/python3
"""script fetchs webpage"""

import sys
import urllib.request
import requests


with urllib.request.urlopen(sys.argv[1]) as response:
    print(response.headers['X-Request-Id'])
