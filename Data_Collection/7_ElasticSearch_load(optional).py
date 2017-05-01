#This script loads all workload data into elastic search
import json
import elasticsearch

es = elasticsearch.Elasticsearch()  # use default of localhost, port 9200

with open("../Temp_Output/Workload_Parsed_JSON_Logs_2.json") as f:
    data = json.load(f)

j = 0
i = len(data)

while j<i:
    print j
    es.index(index='test-index', doc_type='test_workload_logs', id=j+1, body=data[j])
    j = j + 1

#print type(data)
#print data[0]
#print len(data)
