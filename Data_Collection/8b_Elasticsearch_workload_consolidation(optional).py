#Thsi script uses Elasticsearch to search for workload consolidated information
from elasticsearch import Elasticsearch
from elasticsearch_dsl import Search


client = Elasticsearch()


s = Search(using = client,index = 'test-index')

s.aggs.bucket('per_category','terms', field='ProcessId')
s.aggs['per_category'].metric('StartDate', 'min', field='Date')
s.aggs['per_category'].metric('EndDate', 'max', field='Date')

print s.to_dict()

#for hit in s:
    #print(hit.per_category.StartDate)

for tag in s['aggregations']['per_category']['buckets']:
    print(tag['key'], tag['StartDate']['value'])
    
#for hit in response['hits']['hits']:
    #print(hit['_score'], hit['_source']['Severity'])

#for tag in response['aggregations']['ProcessId']['buckets']:
    #print(tag['key'], tag['max_lines']['value'])
