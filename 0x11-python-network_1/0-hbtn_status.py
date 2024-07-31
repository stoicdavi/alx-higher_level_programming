#!/usr/bin/python3
"""
script to fetch https://alx-intranet.hbtn.io/status
"""
import urllib.request
with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as response:
    html = response.read()
    print("Body response:")
    print(f"\t- type: {type(html)}")
    print(f"\t- content: {html}")
    print("\t- utf8 content: {}".format(html.decode('utf-8')))
