#!/bin/bash
# Send a DELETE request to a given URL and display the response body.
methods=$(curl -s -X OPTIONS "\$1" -I | grep -i "Allow:" | cut -d' ' -f2-)

