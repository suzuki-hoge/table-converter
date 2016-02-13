#!/bin/env python2.7

import sys
sys.dont_write_bytecode = True

import os.path
toolPath = "%s/%s" % (os.path.dirname(os.path.abspath(__file__)), 'to-markdown.py')

import commands

def _mkCsv(lines):
    return r'\\n'.join(lines)

def test(inLines, expectedLines):
    csv = _mkCsv(inLines)
    markdown = commands.getoutput('echo "%s" | python %s' % (csv, toolPath))
    expeced = '\n'.join(expectedLines)
    assert markdown == expeced, '\n\nmarkdown:\n%s\n\nexpected:\n%s' % (markdown, expeced)
    
# main
test(
        [
            'header1,header2',
            'element1,element2',
            'element3,element4',
        ],
        [
            'header1  | header2 ',
            ':--      | :--     ',
            'element1 | element2',
            'element3 | element4',
        ]
)
    
# trim
test(
        [
            'header1,      header2',
            'element1,  element2',
        ],
        [
            'header1  | header2 ',
            ':--      | :--     ',
            'element1 | element2',
        ]
)
    
# one row
test(
        [
            'header1,header2'
        ],
        [
            'header1 | header2',
            ':--     | :--    '
        ]
)
    
# short cols
test(
        [
            'h1,h2',
            'e1,e2',
        ],
        [
            'h1  | h2 ',
            ':-- | :--',
            'e1  | e2 '
        ]
)
    
# empty input
test(
        [],
		['to-markdown.py error: input csv is empty']
)
    
# deviated columns
test(
        [
            'h1,h2',
            'e1,e2',
            'e3,e4,e5',
            'e6,e7',
            'e8'
        ],
        [
			'to-markdown.py error: not match each colmun count',
            ' 2: h1,h2',
            ' 2: e1,e2',
            ' 3: e3,e4,e5',
            ' 2: e6,e7',
            ' 1: e8'
        ]
)
