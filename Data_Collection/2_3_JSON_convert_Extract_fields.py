#This script converts error logs that were extracted from Splunk into JSON format and removes unwanted fields from each log entry
import json
import re

with open("../Temp_Output/ErrorLogs.json") as f:
    content = f.readlines()

#print content[0]
try:    
    f2 = open("../Temp_Output/Temp_JSON.txt","w+")
    f3 = open("../Temp_Output/JSON_ErrorLogs.json","a+")
    f4 = open("../Temp_Output/Parsed_JSON_ErrorLogs.json","a+")

    i = len(content)
    j = 0

    while j<i:
        json_string = content[j]
        parsed_json = json.loads(json_string)
        #print type(parsed_json)
        #print parsed_json.items()
        json.dump(parsed_json,f3)
        j = j + 1

        data = parsed_json
        #print data
        #print data
        #print type(data)
        #print set(data.keys())
        #print data['result'].keys()
        unwanted = set(data.keys()) - {'result'}
        for unwanted_key in unwanted: del data[unwanted_key]
        #print data
        unwanted = set(data['result'].keys()) - {'_time','host','_raw'}
        for unwanted_key in unwanted: del data['result'][unwanted_key]
        #re.sub("\nMessage:\w+[\s\S]+\nSeverity","\nSeverity",data['result']['_raw'])
        a = re.search(r"\nMessage",data['result']['_raw'])
        b = re.search(r"\nSeverity",data['result']['_raw'])
        if (a!=None and b!=None):
            data['result']['_raw'] = data['result']['_raw'][0:a.start()]+" "+data['result']['_raw'][b.start()+1:]
        #print data
        if (data.has_key('ProcessId')==False and data.has_key('ThreadId')==False):
            c = re.search(r"Process Id: ",data['result']['_raw'])
            d = re.search(r"Thread Id: ",data['result']['_raw'])
            e = re.search(r"\n",data['result']['_raw'][c.end()+1:])
            q = re.search(r"\n",data['result']['_raw'][d.end()+1:])
            g = re.search(r"Severity: ",data['result']['_raw'])
            h = re.search(r"\n",data['result']['_raw'][g.end()+1:])
            data['result']['Severity'] = data['result']['_raw'][g.end():g.end()+h.start()+1]
            listint1 = [int(s) for s in data['result']['_raw'][c.end():c.end()+e.start()+1].split() if s.isdigit()]
            data['result']['ProcessId'] = listint1[0]
            listint2 = [int(s) for s in data['result']['_raw'][d.end():d.end()+q.start()+1].split() if s.isdigit()]
            data['result']['ThreadId'] = listint2[0]
            l = re.search(r'\d{4}-\d{2}-\d{2}', data['result']['_time'])
            data['result']['Date'] = data['result']['_time'][l.start():l.end()]
            k = re.search(r'\d{2}\:\d{2}\:\d{2}\.\d{3}', data['result']['_time'])
            data['result']['Time'] = data['result']['_time'][k.start():k.end()]
            print data
        #parsed_json = json.loads(data)
        json.dump(data,f4)
finally:
    f2.close()
    f3.close()
    f4.close()

#Close the file
#f2.close()
#f3.close()
#f4.close()


