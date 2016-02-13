cd `dirname $0`

echo '\ncsv -> markdown'
cat valid.csv | python ../api/to-markdown.py                                                                                                                                                       master
echo '\ncsv -> markdown'
cat invalid.csv | python ../api/to-markdown.py                                                                                                                                                       master

echo '\nmarkdown -> csv'
cat valid.md | python ../api/to-csv.py                                                                                                                                                       master
echo '\nmarkdown -> csv'
cat invalid.md | python ../api/to-csv.py
