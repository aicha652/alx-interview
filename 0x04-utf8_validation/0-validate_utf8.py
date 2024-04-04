#!/usr/bin/python3
""" method that determines if a given data
set represents a valid UTF-8 encoding"""


def validUTF8(data):
    """define a function"""
    for item in data:
        try:
            data_decode = data.decode('utf-8')
        except UnicodeDecodeError:
            return False
    return True