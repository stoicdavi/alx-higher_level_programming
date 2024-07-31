#!/usr/bin/python3
"""
script to print the x-request-id
"""
import urllib.request
import sys
if __name__ == "__main__":
    url = sys.argv[1]
    with urllib.request.urlopen(url) as response:
        headers = dict(response.info())
        print(headers.get("X-Request-Id"))
