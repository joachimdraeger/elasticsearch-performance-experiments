python metrics.py
siege -r 1000 -c 1 --content-type="application/json" http://localhost:9200/$1'/_search?request_cache=false&size=0 POST < '$2
python metrics.py
