#!/bin/env python2.7

import sys
sys.dont_write_bytecode = True

import os.path
toMarkdown = "%s/%s" % (os.path.dirname(os.path.abspath(__file__)), 'to-markdown.py')
toCsv = "%s/%s" % (os.path.dirname(os.path.abspath(__file__)), 'to-csv.py')

import commands

def testToMarkdown(inLines, expectedLines):
    _test(toMarkdown, inLines, expectedLines)

def testToCsv(inLines, expectedLines):
    _test(toCsv, inLines, expectedLines)

def _test(toolPath, inLines, expectedLines):
    inLine = r'\\n'.join(inLines)
    expectedLine = '\n'.join(expectedLines)

    response = commands.getoutput('echo "%s" | python %s' % (inLine, toolPath))

    assert response == expectedLine, '\n\nresponse:\n%s\n\nexpected:\n%s' % (response, expectedLine)
    
# main
testToMarkdown(
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
testToMarkdown(
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
testToMarkdown(
        [
            'header1,header2'
        ],
        [
            'header1 | header2',
            ':--     | :--    '
        ]
)
    
# short cols
testToMarkdown(
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
testToMarkdown(
        [],
		['error at api: input is empty']
)
    
# deviated columns
testToMarkdown(
        [
            'h1,h2',
            'e1,e2',
            'e3,e4,e5',
            'e6,e7',
            'e8'
        ],
        [
			'error at api: not match each colmun count',
            ' 2: h1,h2',
            ' 2: e1,e2',
            ' 3: e3,e4,e5',
            ' 2: e6,e7',
            ' 1: e8'
        ]
)

# main
testToCsv(
        [
            'header1  | header2 ',
            ':--      | :--     ',
            'element1 | element2',
            'element3 | element4',
        ],
        [
            'header1,header2',
            'element1,element2',
            'element3,element4',
        ]
)

# empty input
testToCsv(
        [],
		['error at api: input is empty']
)

# deviated columns
testToCsv(
        [
            'h1  | h2 ',
            ':-- | :--',
            'e1  | e2  | e3'
        ],
        [
			'error at api: not match each colmun count',
            ' 2: h1  | h2',
            ' 2: :-- | :--',
            ' 3: e1  | e2  | e3'
        ]
)

# no aligns line
testToCsv(
        [
            'h1 | h2',
            'e1 | e2'
        ],
        ['error at api: no aligns line']
)
