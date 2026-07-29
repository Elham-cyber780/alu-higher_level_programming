#!/bin/bash
# Sends a request to a URL and displays the size of the body in bytes
curl -s -o /tmp/curl_body "$1" && wc -c < /tmp/curl_body | tr -d ' '
