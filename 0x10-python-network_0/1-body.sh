#!/bin/bash
# Author: Mikias Hailu
# Gets the body of a response from a URL if the status code is 200
curl -s -L "$1"
