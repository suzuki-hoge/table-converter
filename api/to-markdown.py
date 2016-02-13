#!/bin/env python2.7

import sys
sys.dont_write_bytecode = True

def getLines(f):
    return f()

def dummy():
    return ['Title,Hero,Boss',
            'MGS,Solid Snake,Liquid Snake',
            'MGS2,Raiden,Solidus Snake',
            'MGS3,Naked Snake,The Boss']

def empty():
    return []

def invalidCols():
    return ['a, b', 'c, d, e', 'f, g']

def stdin():
    [line.strip() for line in sys.stdin.readlines()]

lines = getLines(invalidCols)

from converter import toMarkdown

try:
    print toMarkdown(lines)
except AssertionError, e:
    print e
