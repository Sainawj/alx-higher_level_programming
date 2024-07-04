#!/bin/bash
# Sends an OPTIONS HTTP request to a server and retrieves allowed methods
curl -s -I -X OPTIONS "$1" | grep 'Allow:' | cut -f2- -d' '
