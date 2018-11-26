curl -H "Content-Type: application/json" 'http://localhost:9200/'$1'/_search?request_cache=false&pretty' -d @$2 
