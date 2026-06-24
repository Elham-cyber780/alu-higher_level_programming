#!/usr/bin/python3
def uppercase(str):
    """Print string in uppercase"""
    for c in str:
        if ord(c) >= 97 and ord(c) <= 122:
            print("{:s}".format(chr(ord(c) - 32)), end="")
        else:
            print("{:s}".format(c), end="")
    print("")
