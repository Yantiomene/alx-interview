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
            if byte >> 7 == 0:
                continue
            
            while byte & (1 << (7 - nbytes)):
                nbytes += 1

            if nbytes == 1 or nbytes > 4:
                print(f"byte: {byte} \nnbytes: {nbytes}")
                return False
            if nbytes == 0:
                continue
        else:
            if not(byte & BIT7 and not(byte & BIT6)):
                print(f"byte: {byte} \nnbytes: {nbytes}")
                return False
            nbytes -= 1
            if nbytes > 0:
                continue

        if nbytes == 2 and byte < (1 << 7 + 1 << 6):
            return False
        elif nbytes == 3 and byte < (1 << 7 + 1 << 6 + 1 << 13):
            return False

    print(f"byte: {byte} \nnbytes: {nbytes}")
    return nbytes == 0
