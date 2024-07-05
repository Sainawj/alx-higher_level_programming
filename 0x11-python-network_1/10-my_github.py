#!/usr/bin/python3
"""
Script that takes your Github credentials and uses
Github API to display your id
"""
import requests
import sys

# GitHub API URL to get user information
url = "https://api.github.com/user"

# Getting username and password from
# command line arguments
username = sys.argv[1]
token = sys.argv[2]

# Making a GET request with Basic Authentication
response = requests.get(url, auth=(username, token))

# Checking if the request was successful
if response.status_code == 200:
    user_data = response.json()
    print(user_data.get("id"))
else:
    print("None")
