#!/usr/bin/python3
"""i
A Python script that accepts a URL, makes a request to it, and
outputs the value of the X-Request-Id variable
from the response header
"""
import requests
from sys import argv

if __name__ == '__main__':
    r = requests.get(argv[1])
    print(r.headers.get('X-Request-Id'))
