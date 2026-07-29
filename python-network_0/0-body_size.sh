#!/bin/bash
# Sends a request to a URL and displays the size of the body in bytes
curl -sl "$1" | wc -c
