# -*- coding: utf-8 -*-

def align(lines):
    colsList = [line.split('|') for line in lines]
    maxWidths = _maxWidths(colsList)
    print maxWidths
    filledColsList = [_fill(cols, maxWidths) for cols in colsList]
    return '\n'.join([' | '.join(filledCols) for filledCols in filledColsList])

def _maxWidths(colsList):
    _pickMax = lambda l1, l2: [max(e1, e2) for e1, e2 in zip(l1, l2)]
    lens = [map(len, cols) for cols in colsList]
    return reduce(_pickMax, lens)
 
def _fill(cols, maxWidths):
    return [(col + ' ' * maxWidth)[:maxWidth] for col, maxWidth in zip(cols, maxWidths)]

align(['あ|う', ':--|:--', 'aaあ|uuう'])
