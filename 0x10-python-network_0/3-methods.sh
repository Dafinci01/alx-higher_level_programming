#!/bin/bash
# Display all HTTP methods the server of 
curl -s -X OPTIONS "$URL" -I | grep -i "allow:" | cut -d ' ' -f2-
