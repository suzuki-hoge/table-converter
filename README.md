# table-converter
Vim上で`csv`と`markdownのテーブル記法`の相互変換を行うVimプラグイン、および変換APIです

## 初期設定
### スクリプト取得
`$ git clone https://github.com/tenshiPure/table-converter.git`

### vimの設定ファイル(~/.vimrc)に設定を追記
```VimScript:~/.vimrc
let g:table_converter_root_path = '/path/to/dir/vim/table-converter'
source /path/to/dir/vim/table-converter/vim/commands.vim
```

## 使い方（Vimプラグイン）
### ToMarkdown
範囲選択中に`:ToMarkdown`と入力すると、現在編集しているファイルの一部を`csv`から`markdown`に変換して書き換えます
![demo](./demo/OK-ToMarkdown.gif)

選択した行のカラム数がずれている等のエラー時には書き換えは行われません
（このエラー時の挙動は他のコマンドも全て同様です）
![demo](./demo/NG-ToMarkdown.gif)

### ShowMarkdown
`ToMarkdown`と違い、変換結果は表示されるだけです
![demo](./demo/OK-ShowMarkdown.gif)

### AppendMarkdownFromFile
`csv`ファイルを読み込み、カーソルの位置に`markdown`を展開します

```
$ cat ../samples/valid.csv
Title,Hero,Boss
MGS,Solid Snake,Liquid Snake
MGS2,Raiden,Solidus Snake
MGS3,Naked Snake,The Boss
```
![demo](./demo/OK-AppendMarkdownFromFile.gif)

### ToCsv
`ToMarkdown`の逆を行います
![demo](./demo/OK-ToCsv.gif)

`csv`に変換するのは何らかの表計算ソフトで編集するためだと思われるので、縦揃えはされず隙間はつめて出力されます  
縦の揃っていない`markdown`に`ToCsv`と`ToMarkdown`を実行すると縦が揃います

### WriteCsvToFile
選択した範囲の`markdown`を`csv`に変換し、ファイルに書き出します
![demo](./demo/OK-WriteCsvToFile.gif)

```
$ cat xxx/out.csv
Title,Hero,Boss
MGS,Solid Snake,Liquid Snake
MGS2,Raiden,Solidus Snake
MGS3,Naked Snake,The Boss
```

（この例では出力先はマスクしていますが、実際にはフルパスが表示されます）

## 使い方（コマンドラインツール）
### to-markdown.py
標準入力で改行を含む文字列を受け取り、標準出力します
```
$ cat valid.csv
Title,Hero,Boss
MGS,Solid Snake,Liquid Snake
MGS2,Raiden,Solidus Snake
MGS3,Naked Snake,The Boss

$ cat valid.csv | python to-markdown.py
Title | Hero        | Boss         
:--   | :--         | :--          
MGS   | Solid Snake | Liquid Snake 
MGS2  | Raiden      | Solidus Snake
MGS3  | Naked Snake | The Boss     
```

### to-csv.py
標準入力で改行を含む文字列を受け取り、標準出力します
```
$ cat valid.md
Title | Hero        | Boss         
:--   | :--         | :--          
MGS   | Solid Snake | Liquid Snake 
MGS2  | Raiden      | Solidus Snake
MGS3  | Naked Snake | The Boss     

$ cat valid.md | python to-csv.py
Title,Hero,Boss
MGS,Solid Snake,Liquid Snake
MGS2,Raiden,Solidus Snake
MGS3,Naked Snake,The Boss
```
