#!/bin/bash
# Send a PUT request with specific data to make the server respond with "You got me!"
curl -s -L -X PUT -d "user_id=98" -H "Origin:Kenya" 0.0.0.0:5000/catch_me
