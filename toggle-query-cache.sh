curl -X POST "localhost:9200/$1/_close"
curl -X PUT "localhost:9200/$1/_settings" -H 'Content-Type: application/json' -d'
{
    "index" : {
        "queries.cache.enabled" : '$2'
    }
}
'
curl -X POST "localhost:9200/$1/_open"
