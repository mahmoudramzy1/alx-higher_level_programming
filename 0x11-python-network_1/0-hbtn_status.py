#!/usr/bin/python3
import urllib.request
import requests

with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as response:
    html = response.read()
print('Body response:')
print('\t- type: ', type(html))
print('\t- content: ', html)
print('\t- utf8 ', html.decode('utf-8'))