#!/usr/bin/python3
"""script fetchs webpage"""

import urllib.request

with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as response:
    html = response.read()
print('Body response:')
print('\t- type:', type(html))
print('\t- content:', html)
print('\t- utf8 content:', html.decode('utf-8'))
