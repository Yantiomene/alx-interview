#!/usr/bin/python3
"""UTF8 validation"""

BIT7 = 1 << 7
BIT6 = 1 << 6


def validUTF8(data):
    """Determines if a given dataset represents a valid
    UTF-8 encoding
    args:
         data: list of integers
    return:
           True or False
    """
    nbytes = 0

    for byte in data:
        if nbytes == 0:
            while byte & (1 << (7 - nbytes)):
                nbytes += 1

            if nbytes == 1 or nbytes > 4:
                return False
            if nbytes == 0:
                continue
        else:
            if not(byte & BIT7 and not(byte & BIT6)):
                return False
            nbytes -= 1

    return nbytes == 0
