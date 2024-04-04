#!/usr/bin/python3
def validUTF8(data):
    try:
        data_decode = data.decode('utf-8')
        return True
    except UnicodeDecodeError:
        return False