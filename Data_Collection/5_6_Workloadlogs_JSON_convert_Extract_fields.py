#Thsi script converts workload logs to JSON format and removes unwanted fields from them
import json
import re
from datetime import datetime as dt

with open("../Temp_Output/Workload_Logs.json") as f:
    content = f.readlines()

#print content[0]

f2 = open("../Temp_Output/Workload_Temp_JSON.txt","w+")
f3 = open("../Temp_Output/Workload_JSON_Logs.json","a+")
f4 = open("../Temp_Output/Workload_Parsed_JSON_Logs_2.json","a+")

f4.write("[")

try:
    i = len(content)
    j = 0
    workload = {}

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
            if (c!=None and d!=None):
                e = re.search(r"\n",data['result']['_raw'][c.end()+1:])
                q = re.search(r"\n",data['result']['_raw'][d.end()+1:])
            g = re.search(r"Severity: ",data['result']['_raw'])
            if (g!=None):
                h = re.search(r"\n",data['result']['_raw'][g.end()+1:])
            l = re.search(r'\d{4}-\d{2}-\d{2}', data['result']['_time'])
            k = re.search(r'\d{2}\:\d{2}\:\d{2}\.\d{3}', data['result']['_time'])
            if (c!=None and d!=None and e!=None and q!=None and g!=None and h!=None and l!=None and k!=None):
                data['result']['Severity'] = data['result']['_raw'][g.end():g.end()+h.start()+1]
                listint1 = [int(s) for s in data['result']['_raw'][c.end():c.end()+e.start()+1].split() if s.isdigit()]
                data['result']['ProcessId'] = listint1[0]
                listint2 = [int(s) for s in data['result']['_raw'][d.end():d.end()+q.start()+1].split() if s.isdigit()]
                data['result']['ThreadId'] = listint2[0]
                data['result']['Date'] = data['result']['_time'][l.start():l.end()]
                data['result']['Time'] = data['result']['_time'][k.start():k.end()]
                print data['result']
        #parsed_json = json.loads(data)
        json.dump(data['result'],f4)
        if (j<i-1):
            f4.write(",")

        #Workload Consolidation
        #if (workload.has_key(data['result']['ProcessId']) == False):
            #workload[data['result']['ProcessId']]={}
            #workload[data['result']['ProcessId']]['StartDate'] = data['result']['Date']
            #workload[data['result']['ProcessId']]['EndDate'] = data['result']['Date']
            #workload[data['result']['ProcessId']]['StartTime'] = data['result']['Time']
            #workload[data['result']['ProcessId']]['EndTime'] = data['result']['Time']
        #else:
            #date1 = dt.strptime(data['result']['Date'], "%Y-%m-%d")
            #date2 = dt.strptime(workload[data['result']['ProcessId']]['StartDate'], "%Y-%m-%d")
            #date3 = dt.strptime(workload[data['result']['ProcessId']]['EndDate'], "%Y-%m-%d")
            #if (date1<date2):
                #workload[data['result']['ProcessId']]['StartDate'] = data['result']['Date']
            #if (date1>date3):
                #workload[data['result']['ProcessId']]['EndDate'] = data['result']['Date']
            #time1 = dt.strptime(data['result']['Time'][:-4], "%H:%M:%S")
            #time2 = dt.strptime(workload[data['result']['ProcessId']]['StartTime'][:-4], "%H:%M:%S")
            #time3 = dt.strptime(workload[data['result']['ProcessId']]['EndTime'][:-4], "%H:%M:%S")
            #if (time1<time2):
                #workload[data['result']['ProcessId']]['StartTime'] = data['result']['Time']
            #if (time1>time3):
                #workload[data['result']['ProcessId']]['EndTime'] = data['result']['Time']
        #print workload

    f4.write("]")
finally:
    f2.close()
    f3.close()
    f4.close()
    
#Close the file
#f2.close()
#f3.close()
#f4.close()

