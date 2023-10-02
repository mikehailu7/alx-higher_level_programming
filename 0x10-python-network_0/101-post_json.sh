#!/bin/bash
#Author: MikiasHailu
curl -sL -X POST -H 'Content-Type: application/json' -d "$([ -f "$2" ] && cat "$2")" "$1"
