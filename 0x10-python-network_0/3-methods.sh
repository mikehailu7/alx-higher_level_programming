#!/bin/bash
# Author: Mikias Hailu
curl -siLk -X OPTIONS "$1" | grep -oiE 'Allow: .+' | cut -d ' ' -f2-
