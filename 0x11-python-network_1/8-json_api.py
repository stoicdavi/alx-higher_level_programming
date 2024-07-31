#!/usr/bin/python3
"""
python script that takes in a letter
and sends a post request to
http://0.0.0.0:5000/search_user with the letter as a parameter
"""
import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) > 1:
        letter = {"q": sys.argv[1]}
    else:
        letter = {"q": ""}
    my_request = requests.post('http://0.0.0.0:5000/search_user', data=letter)
    try:
        response = my_request.json()
        if response:
            print(f"[{response['id']}] {response['name']}")
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
