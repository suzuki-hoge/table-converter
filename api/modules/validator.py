def isValid(lines):
    _isEmpty(lines)
    _isValidCols(lines)

def _isEmpty(lines):
	assert lines != [''], 'to-markdown.py error: input csv is empty'

def _isValidCols(lines):
    colCounts = [line.count(',') for line in lines]
    assert all([colCounts[0] == colCount for colCount in colCounts[1:]]), 'to-markdown.py error: not match each colmun count\n' + '\n'.join(["%2s: %s" % (colCount + 1, line) for colCount, line in zip(colCounts, lines)])

