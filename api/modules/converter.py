from validator import isValid

def toMarkdown(lines):
    isValid(lines)

    convertedLines = [_rowConvert(line) for line in lines]
    aligns = _aligns(convertedLines)

    return convertedLines[:1] + [aligns] + convertedLines[1:]

def _aligns(lines):
    return '|'.join([':--' for _ in lines[0].split('|')])

def _rowConvert(line):
    return '|'.join([col.strip() for col in line.split(',')])
