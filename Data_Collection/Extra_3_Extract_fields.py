#This script removes unwanted fields from error logs which are in JSON format
import json
import re

f3 = open("../Temp_Output/Parsed_JSON_ErrorLogs.json","a+")

with open("../Temp_Output/JSON_ErrorLogs.json") as f:
    data = json.load(f)
    #print data
    #print type(data)
    #print set(data.keys())
    #print data['result'].keys()
    unwanted = set(data.keys()) - {'result'}
    for unwanted_key in unwanted: del data[unwanted_key]
    #print data
    unwanted = set(data['result'].keys()) - {'_time','host','_raw'}
    for unwanted_key in unwanted: del data['result'][unwanted_key]
    a = re.search(r"\nMessage",data['result']['_raw'])
    b = re.search(r"\nSeverity",data['result']['_raw'])
    data['result']['_raw'] = data['result']['_raw'][0:a.start()]+" "+data['result']['_raw'][b.start()+1:]
    print data
    #parsed_json = json.loads(data)
    #json.dump(parsed_json,f3)

f3.close()
