command! -range ShowMarkdown <line1>,<line2>call ShowMarkdown()
command! -range ToMarkdown <line1>,<line2>call ToMarkdown()

function! ShowMarkdown() range
    echo s:getMarkdown(a:firstline, a:lastline)
endfunction

function! ToMarkdown() range
    let markdown = s:getMarkdown(a:firstline, a:lastline)
    if s:isValidResponse(markdown)
        call s:updateLines(a:firstline, a:lastline, markdown)
    else
        echo markdown
    endif
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

function! s:updateLines(first, last, markdown)
    let lines = split(a:markdown, '\n')
    for linenum in range(a:first, a:last)
        call setline(linenum, lines[linenum - a:first])
    endfor
    call append(a:last, lines[-1])
endfunction

function! s:isValidResponse(markdown)
    return split(a:markdown, '\n')[0] !~# '^to-markdown.py error:'
endfunction
