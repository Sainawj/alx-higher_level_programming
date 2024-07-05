#!/usr/bin/python3
"""
Script that fetches https://intranet.hbtn.io/status
"""
import requests

url = "https://alx-intranet.hbtn.io/status"

# Fetching the URL using requests
response = requests.get(url)
body = response.text

# Displaying the response body
print("Body response:")
print("\t- type: {}".format(type(body)))
print("\t- content: {}".format(body))
