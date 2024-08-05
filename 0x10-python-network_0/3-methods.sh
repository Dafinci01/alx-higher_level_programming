#!/bin/bash
# Display all HTTP methods the server of curl methods 
curl -sl "$1" | grep "Allow" | cut -d " " -f 2-
