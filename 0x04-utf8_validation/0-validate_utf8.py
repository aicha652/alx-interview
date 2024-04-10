#!/usr/bin/python3
""" method that determines if a given data
set represents a valid UTF-8 encoding"""


def validUTF8(data):
    """define a function"""
    try:
        if any(not 0 <= byte <= 255 for byte in data):
            return False
        data_byte = bytes(data)
        data_byte.decode('utf-8')
        return True
    except UnicodeDecodeError:
        return False
