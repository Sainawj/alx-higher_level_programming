#!/bin/bash
# bash script to display status code of the server
curl -L -s -X HEAD -w "%{http_code}" "$1"
