import sys
import json

for line in sys.stdin:
    doc = json.loads(line)
    date = doc['published'][:10]
    if date > "2015-09-01":
        print('{ "index" : { "_index" : "articles-daily-' + date + '", "_type" : "_doc"}')
        print(line[:-1])
