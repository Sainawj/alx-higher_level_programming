#!/usr/bin/env python3
def no_c(myString):
    nString = ''
    for char in myString:
        if char != 'c' and char != 'C':
            nString += char
    return nString
