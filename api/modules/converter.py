from validator import isValidCsv, isValidMarkdown

def toMarkdown(lines):
    isValidCsv(lines)

    convertedLines = [_rowConvert(line, ',', '|') for line in lines]
    aligns = '|'.join([':--' for _ in convertedLines[0].split('|')])

    return convertedLines[:1] + [aligns] + convertedLines[1:]

def toCsv(lines):
    isValidMarkdown(lines)

    convertedLines = [_rowConvert(line, '|', ',') for line in lines]

    return convertedLines[:1] + convertedLines[2:]

def _rowConvert(line, f, t):
    return t.join([col.strip() for col in line.split(f)])
