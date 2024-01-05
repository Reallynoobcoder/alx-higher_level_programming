#!/bin/bash
#Displays the size of the body of the response
curl -sI $@ | grep 'Content-Length:' | cut -d ' ' -f2
