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

def stdin():
    [line.strip() for line in sys.stdin.readlines()]

lines = getLines(dummy)

from converter import toMarkdown

markdown = toMarkdown(lines)
print markdown
