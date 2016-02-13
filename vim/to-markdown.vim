command! -range ShowMarkdown <line1>,<line2>call ShowMarkdown()
command! -range ToMarkdown <line1>,<line2>call ToMarkdown()
command! -nargs=1 -complete=file AppendMarkdown call AppendMarkdown(<f-args>)

let s:toolPath = fnamemodify('.', ':p') . '../api/to-markdown.py'

function! ShowMarkdown() range
    echo s:getMarkdown(a:firstline, a:lastline)
endfunction

function! ToMarkdown() range
    let markdown = s:getMarkdown(a:firstline, a:lastline)

    if s:isValidResponse(markdown)
        let lines = split(markdown, '\n')
        for linenum in range(a:firstline, a:lastline)
            call setline(linenum, lines[linenum - a:firstline])
        endfor
        call append(a:lastline, lines[-1])

    else
        echo markdown

    endif
endfunction

function! AppendMarkdown(path)
    let markdown = system('cat ' . a:path . ' | python ' . s:toolPath)

    if s:isValidResponse(markdown)
        let lines = split(markdown, '\n')
        call append(line('.'), lines)

    else
        echo markdown

    endif
endfunction

function! s:getMarkdown(first, last)
    let lines = getline(a:first, a:last)
    let line = join(lines, '\\n')
    return system('echo "' . line . '" | python ' . s:toolPath)
endfunction

function! s:isValidResponse(markdown)
    return split(a:markdown, '\n')[0] !~# '^to-markdown.py error:'
endfunction
