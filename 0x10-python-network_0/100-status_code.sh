#!/bin/bash
#Author: MikiasHailu
curl -s -w "%{response_code}" -o /dev/null "$1"
