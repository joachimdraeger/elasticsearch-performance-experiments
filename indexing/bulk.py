import requests
import sys
import json

def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)

def bulk(payload):
    r = requests.post(
        'http://localhost:9200/_bulk',
        headers={'Content-Type':
        'application/x-ndjson'},
        data=payload)
    r.raise_for_status()
    result = json.loads(r.text)
    if result["errors"]:
        raise(Exception('bulk request result contains errors'))

payload = ""
counter = 0
for line in sys.stdin:
    payload += line
    counter += 1
    if counter % 200 == 0:
        bulk(payload)
        payload = ""
        eprint(counter)

if len(payload) > 0:
    bulk(payload)
