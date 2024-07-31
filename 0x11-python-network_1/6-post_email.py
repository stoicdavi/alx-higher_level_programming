#!/usr/bin/python3
"""
python scipt that takes in url and email as arguments
sends a post request to the passed url
"""
import requests
import sys
if __name__ == "__main__":
    myurl = sys.argv[1]
    mail = {"email": sys.argv[2]}
    r = requests.post(myurl, data=mail)
    print(r.text)
