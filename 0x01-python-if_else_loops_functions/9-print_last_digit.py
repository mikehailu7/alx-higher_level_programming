#!/usr/bin/python3
def print_last_digit(number):
    """This will print the last digit of a number"""
    lasDig = abs(number) % 10
    print(f"{lasDig}", end, end='')
    return lasDig
