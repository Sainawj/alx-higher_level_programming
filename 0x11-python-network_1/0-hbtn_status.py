#!/usr/bin/python3
"""Script to fetch data from
    https://alx-intranet.hbtn.io/status
"""
import urllib.request

url = "https://alx-intranet.hbtn.io/status"

# Fetching the URL using urllib
with urllib.request.urlopen(url) as response:
    body = response.read()

# Displaying the response body
print("Body response:")
print("\t- type: {}".format(type(body)))
print("\t- content: {}".format(body))
print("\t- utf8 content: {}".format(body.decode('utf-8')))
