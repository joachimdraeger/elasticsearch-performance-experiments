gunzip -c ../signalmedia-1m.jsonl.gz | python jsonl2bulk-daily.py | python bulk.py
