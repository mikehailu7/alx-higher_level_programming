#!/bin/bash
# Author: Mikias Hailu
# This will get the size of the body of a response from a URL
curl -sI $1 | grep "Content-Length" | cut -d " " -f2
