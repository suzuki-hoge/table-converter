def isValidCsv(lines):
    _isEmpty(lines)
    _isValidCols(lines, ',')

def isValidMarkdown(lines):
    _isEmpty(lines)
    _isValidCols(lines, '|')
    assert ':--' in lines[1], 'error at api: no aligns line'

def _isEmpty(lines):
	assert lines != [''], 'error at api: input is empty'

def _isValidCols(lines, sep):
    colCounts = [line.count(sep) for line in lines]
    assert all([colCounts[0] == colCount for colCount in colCounts[1:]]), 'error at api: not match each colmun count\n' + '\n'.join(["%2s: %s" % (colCount + 1, line) for colCount, line in zip(colCounts, lines)])
