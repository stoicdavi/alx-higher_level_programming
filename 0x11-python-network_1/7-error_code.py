#!/usr/bin/python3
"""
this script take in a url
sends a request to the url
and displays the response
"""
import requests
import sys
if __name__ == "__main__":
    myurl = sys.argv[1]
    my_request = requests.get(myurl)
    response = my_request.status_code
    if response >= 400:
        print(f"Error code: {response}")
    else:
        print(my_request.text)
