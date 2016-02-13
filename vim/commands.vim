command! -range                         ShowMarkdown           <line1>,<line2>call ShowMarkdown()
command! -range                         ToMarkdown             <line1>,<line2>call s:insert(s:toMarkdown)
command!        -nargs=1 -complete=file AppendMarkdownFromFile                call AppendMarkdownFromFile(<f-args>)

command! -range                         ToCsv                  <line1>,<line2>call s:insert(s:toCsv)
command! -range -nargs=1 -complete=file WriteCsvToFile         <line1>,<line2>call WriteCsvToFile(<f-args>)


" todo bug
let s:toMarkdown = fnamemodify('.', ':p') . '../api/to-markdown.py'
let s:toCsv = fnamemodify('.', ':p') . '../api/to-csv.py'


function! ShowMarkdown() range
    echo s:getResponse(a:firstline, a:lastline, s:toMarkdown)
endfunction


function! s:insert(toolPath) range
    let response = s:getResponse(a:firstline, a:lastline, a:toolPath)

    if s:isValidResponse(response)
        let lines = split(response, '\n') + ['']
        exec 'normal ' . (a:lastline - a:firstline + 1) . 'dd'
        call append(a:firstline, lines)
        exec 'normal dd'
    else
        echo response
    endif
endfunction


function! AppendMarkdownFromFile(path)
    let response = system('cat ' . a:path . ' | python ' . s:toMarkdown)

    if s:isValidResponse(response)
        let lines = split(response, '\n')
        call append(line('.'), lines)
    else
        echo response
    endif
endfunction


function! WriteCsvToFile(path) range
    let response = s:getResponse(a:firstline, a:lastline, s:toCsv)

    if s:isValidResponse(response)
        let lines = split(response, '\n')
		call writefile(lines, a:path)
		echo 'write: ' . a:path
    else
        echo response
    endif
endfunction


function! s:getResponse(first, last, toolPath)
    let lines = getline(a:first, a:last)
    let line = join(lines, '\\n')
    return system('echo "' . line . '" | python ' . a:toolPath)
endfunction


function! s:isValidResponse(response)
    return split(a:response, '\n')[0] !~# '^error at api'
endfunction
