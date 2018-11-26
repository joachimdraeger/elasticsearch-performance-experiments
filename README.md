# Elasticsearch Performance Experiments

Demonstrates an approach to understanding performance cost of a single search

## Prerequisites

* 16G RAM, 8G might work when reducing JVM memory to 2G in docker-compose.yml
* 15G disk space to index in three different ways, SSD preferred
* Tested on Mac OS X, should work (better) on Linux
* Docker
* Python 3 with requests package
* Siege (available on most package managers) https://www.joedog.org/siege-manual/
* Download https://research.signalmedia.co/newsir16/signal-dataset.html

## Starting up the Docker Compose stack

```
docker-compose up
```

You can now access Elasticsearch on http://localhost:9200 and Kibana on http://localhost:5601

## Indexing the articles

Create indices and templates:
```
cd index-creation/
./create-articles-1-index.sh
./create-articles-5-index.sh
./create-articles-daily-template.sh
cd ..
```

Indexing:

* Indexing articles-1 and articles-5 took about 15min each on my Macbook
* Indexing articles-daily took 55 min
* The line progress counter will go up to 2 million
```
cd indexing/
./index-articles-1.sh
./index-articles-5.sh
./index-daily.sh
cd ..
```

## Do some testing

See what the example searches return:
```
./search.sh articles-1 vw-query-4.json
./search.sh articles-1 vw-query-16.json
```

For cleaner results, stop Kibana:
```
docker-compose stop kibana
```

This how to run all combinations of indices and searches.
Do a warm-up run first, we don't care about IO.
```
./siege1000.sh articles-1 vw-query-4.json
./siege1000.sh articles-1 vw-query-16.json
./siege1000.sh articles-5 vw-query-4.json
./siege1000.sh articles-5 vw-query-16.json
./siege1000.sh articles-daily vw-query-4.json
./siege1000.sh articles-daily vw-query-16.json
```

The siege script disables the request cache. Check the `indices.query_cache.hit_count` metric and consider disabling the query cache for another round of testing:
```
./toggle-query-cache.sh articles-1 false
./toggle-query-cache.sh articles-5 false
```
