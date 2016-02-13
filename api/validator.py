def isValid(lines):
    _isEmpty(lines)
    _isValidCols(lines)

def _isEmpty(lines):
    assert len(lines) != 0, 'input csv is empty'

def _isValidCols(lines):
    colCounts = [line.count(',') for line in lines]
    assert reduce(lambda x, y: x == y, colCounts), 'not match each colmun count\n' + '\n'.join(["%2s: %s" % (t[0], t[1]) for t in zip(colCounts, lines)])
