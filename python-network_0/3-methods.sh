#!/bin/bash
# Displays all HTTP methods the server will accept for a URL
curl -s -X OPTIONS "$1" -v 2>&1 | grep "Allow:" | cut -d' ' -f2-
