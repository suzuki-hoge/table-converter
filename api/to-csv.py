#!/bin/env python2.7

import sys
sys.dont_write_bytecode = True

lines = [line.strip() for line in sys.stdin.readlines()]

from modules.converter import toCsv

try:
    print '\n'.join(toCsv(lines))
except AssertionError, e:
    print e
