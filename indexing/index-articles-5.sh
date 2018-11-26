gunzip -c ../signalmedia-1m.jsonl.gz | python jsonl2bulk.py articles-5 | python bulk.py
