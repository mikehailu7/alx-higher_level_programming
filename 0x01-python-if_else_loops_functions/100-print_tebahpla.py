#!/usr/bin/python3
for m in range(26):
    if m % 2 == 0:
        print('{:c}'.format(122 - m), end='')
    else:
        print('{:c}'.format(90 - m), end='')
