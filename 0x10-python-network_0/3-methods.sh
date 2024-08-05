#!/bin/bash
#curl method scrpt  to get post, delete and allow from a web
curl -sI "$1" | grep -i '^Allow:' | cut -d ':' -f2- | tr -d ' '
