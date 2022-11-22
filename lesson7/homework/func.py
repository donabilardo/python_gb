import re

def formatStr(data):
    result = "".join(c for c in data if c.isalpha() and " ")
    return result

def joinStr(a,b,c = ""):
    result = a + " " + b + " " + c
    return result

def formatInt(data):
    result = "".join(c for c in data if  c.isdecimal())
    return result
