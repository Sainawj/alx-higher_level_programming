#!/bin/bash
# Sends custom headers to a server using curl
curl -s -H "X-School-User-Id: 98" "$1"
