#This script uses elastic search to search for workload consolidated information
import json
import elasticsearch

es = elasticsearch.Elasticsearch()  # use default of localhost, port 9200

matches = es.search(index='test-index',q='Severity:"Warning"')
hits = matches['hits']['hits']
if not hits:
    print('No matches found')
else:
    #if raw_result:
    print(json.dumps(matches, indent=4))
    for hit in hits:
        print('Severity:{}\nTime: {}\n\n'.format(hit['_source']['Severity'],hit['_source']['Time']))

#print type(data)
#print data[0]
#print len(data)
