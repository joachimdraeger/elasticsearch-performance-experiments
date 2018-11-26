curl \
  -H "Content-Type: application/json" \
  -XPUT http://localhost:9200/_template/articles-daily \
  -d @articles-daily-template.json
