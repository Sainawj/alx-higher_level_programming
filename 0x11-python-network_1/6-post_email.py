#!/usr/bin/python3
"""
A script that accepts a URL and an email address, sends a
POST request to the specified URL with the email as a
parameter, and then displays the response body
"""
import requests
from sys import argv

if __name__ == '__main__':
    payload = {'email': argv[2]}
    r = requests.post(argv[1], data=payload)
    print(r.text)
