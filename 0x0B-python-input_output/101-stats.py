#!/usr/bin/python3
# Author: MikiasHailu
# Project: Logparsing
""" This function wil read stdln and compute a matrix """
import sys

f_size = 0
status_tally = {"200": 0, "301": 0, "400": 0, "401": 0, "403": 0, "404": 0, "405": 0, "500": 0}
m = 0
try:
    for line in sys.stdin:
        tokens = line.split()
        if len(tokens) >= 2:
            z = m
            if tokens[-2] in status_tally:
                status_tally[tokens[-2]] += 1
                m = m + 1
            try:
                f_size += int(tokens[-1])
                if z == m:
                    m = m + 1
            except FileNotFoundError:
                if z == m:
                    continue
        if m % 10 == 0:
            print("File size: {:d}".format(f_size))
            for key, value in sorted(status_tally.items()):
                if value:
                    print("{:s}: {:d}".format(key, value))
    print("File size: {:d}".format(f_size))
    for key, value in sorted(status_tally.items()):
        if value:
            print("{:s}: {:d}".format(key, value))

except KeyboardInterrupt:
    print("File size: {:d}".format(f_size))
    for key, value in sorted(status_tally.items()):
        if value:
            print("{:s}: {:d}".format(key, value))
