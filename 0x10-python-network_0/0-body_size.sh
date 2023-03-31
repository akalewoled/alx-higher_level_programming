#!/bin/bash
#send a request to url with curl and display size of response

curl -s "$1" | wc -c
