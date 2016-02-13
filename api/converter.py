def toMarkdown(lines):
    header = _header(lines)
    aligns = _aligns(header)
    body = _body(lines)

    return '\n'.join([header, aligns, body])

def _header(lines):
    return lines[0].replace(',', '|')

def _aligns(header):
    return '|'.join([':--'] * len(header.split('|')))

def _body(lines):
    return '\n'.join([line.replace(',', '|') for line in lines[1:]])
