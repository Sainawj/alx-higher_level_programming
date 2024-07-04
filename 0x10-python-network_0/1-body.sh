#!/bin/bash
# Send GET request, display body if status code is 20
if [ $(curl -L -s -X HEAD -w "%{http_code}" "$1") == '200' ]; then curl -Ls "$1"; fi
