import sys
import json

index = sys.argv[1]

for line in sys.stdin:
    print('{ "index" : { "_index" : "' + index + '", "_type" : "_doc"}')
    print(line[:-1])
