# Elasticsearch Performance Experiments

Demonstrates an approach to understanding performance cost of a single search

## Prerequisites

* 16G RAM, 8G might work when reducing JVM memory to 2G in docker-compose.yml
* 15G disk space to index in three different ways, SSD preferred
* Tested on Mac OS X, should work (better) on Linux
* Docker
* Python 3 with requests package
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
