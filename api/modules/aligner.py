import unicodedata

def align(lines):
    colsList = [line.split('|') for line in lines]
    maxWidths = _maxWidths(colsList)
    filledColsList = [_fill(cols, maxWidths) for cols in colsList]
    return '\n'.join([' | '.join(filledCols) for filledCols in filledColsList])

def _maxWidths(colsList):
    _pickMax = lambda l1, l2: [max(e1, e2) for e1, e2 in zip(l1, l2)]
    lens = [map(_strwidth, cols) for cols in colsList]
    return reduce(_pickMax, lens)
 
def _strwidth(s):
    return sum([_charwidth(c) for c in s.decode('utf-8')])

def _charwidth(c):
    return 2 if unicodedata.east_asian_width(c) in ['F', 'W', 'A'] else 1

def _fill(cols, maxWidths):
    return [(col + ' ' * (maxWidth - _strwidth(col))) for col, maxWidth in zip(cols, maxWidths)]
