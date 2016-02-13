command! -range ShowMarkdown <line1>,<line2>call ShowMarkdown()

function! ShowMarkdown() range
    echo s:getMarkdown(a:firstline, a:lastline)
endfunction

function! s:getMarkdown(first, last)
    let lines = s:getLines(a:first, a:last)
    return s:callApi(lines)
endfunction

function! s:getLines(first, last)
    return getline(a:first, a:last)
endfunction

function! s:callApi(lines)
    let line = join(a:lines, '\\n')
    let toolPath = fnamemodify('.', ':p') . '../api/to-markdown.py'
    return system('echo "' . line . '" | python ' . toolPath)
endfunction
