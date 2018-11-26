import requests
import time
import json
import os.path
import argparse
from collections import defaultdict

METRICS_LIST = [
    "jvm.gc.collectors.young.collection_count",
    "jvm.gc.collectors.young.collection_time_in_millis",
    "jvm.gc.collectors.old.collection_count",
    "jvm.gc.collectors.old.collection_time_in_millis",
    "thread_pool.search.rejected",
    "indices.search.query_total",
    "indices.search.query_time_in_millis",
    "indices.query_cache.total_count",
    "indices.query_cache.hit_count",
    "indices.query_cache.miss_count",
    "indices.query_cache.cache_size",
    "indices.query_cache.cache_count",
    "indices.query_cache.evictions",
    "indices.request_cache.evictions",
    "indices.request_cache.hit_count",
    "indices.request_cache.miss_count",
    "process.cpu.total_in_millis",
    "fs.io_stats.total.read_operations",
    "fs.io_stats.total.write_operations",
    "fs.io_stats.total.read_kilobytes",
    "fs.io_stats.total.write_kilobytes"
]

METRICS_FILE = 'metrics.json'

def parse_args():
    parser = argparse.ArgumentParser(
        description='arguments'
    )
    parser.add_argument(
        '-e', '--elasticsearch-url',
        metavar='elasticsearch_url',
        required=False,
        help='server url from the elasticsearch api',
        default=os.getenv('ES_URL', 'http://localhost:9200')
    )
    return parser.parse_args()

def get_metric_by_ref(obj, ref, default=None):
    val = obj
    for key in ref.split('.'):
        if key in val:
            val = val[key]
        else:
            return default
    return val

def get_metrics(url):
    node_data = requests.get(url).json()
    metrics = defaultdict(lambda : 0)
    metrics['time'] = time.time()
    for node in node_data['nodes']:
        for metric in METRICS_LIST:
            metrics[metric] += get_metric_by_ref(node_data, '.'.join(['nodes', node, metric]), 0)
    return metrics

def calc_deltas(previous_metrics, metrics):
    deltas = {}
    for k, v in previous_metrics.items():
        deltas[k] = metrics[k] - v
    return deltas

def load_metrics():
    if os.path.isfile(METRICS_FILE):
        with open(METRICS_FILE, 'r') as input:
            return json.load(input)
    else:
        return None

def save_metrics(metrics):
    with open(METRICS_FILE, 'w') as output:
        json.dump(metrics, output)

if __name__ == '__main__':
    args = parse_args()
    metrics = get_metrics(args.elasticsearch_url + "/_nodes/stats")
    previous_metrics = load_metrics()
    if previous_metrics:
        deltas = calc_deltas(previous_metrics, metrics)
        print('Deltas:')
        for k, v in sorted(deltas.items()):
            print (k, v)
    else:
        print('First run, no delta.')
    save_metrics(metrics)
