from validator import isValid

def toMarkdown(lines):
    isValid(lines)

    header = _header(lines)
    aligns = _aligns(header)
    body = _body(lines)

    return [header] + [aligns] + body

def _header(lines):
    return lines[0].replace(',', '|')

def _aligns(header):
    return '|'.join([':--'] * len(header.split('|')))

def _body(lines):
    return [line.replace(',', '|') for line in lines[1:]]

# todo trim
