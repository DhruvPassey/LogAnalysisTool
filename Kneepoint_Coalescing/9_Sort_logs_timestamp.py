#This script sorts all logs based on timestamp to perform coalescing.
import json
import time
from operator import itemgetter
from datetime import datetime

with open("../Temp_Output/Workload_Parsed_JSON_Logs_2.json") as f:
    data = json.load(f)

f4 = open("../Temp_Output/Sorted_Workload_Parsed_JSON_Logs_2.json","a+")

i = len(data)
j = 0

while j<i:
    data[j]['StructTimestamp'] = time.strptime(data[j]['_time'],"%Y-%m-%d %H:%M:%S.%f India Standard Time")
    #print data[j]
    print j
    j = j+1

sorteddata = sorted(data, key=itemgetter('StructTimestamp'))

f4.write("[")

i = len(sorteddata)
j = 0

while j<i:
    if 'StructTimestamp' in sorteddata[j]:
        del sorteddata[j]['StructTimestamp']
    json.dump(sorteddata[j],f4)
    if (j<i-1):
        f4.write(",")
    j = j+1

f4.write("]")

f4.close()

#i = len(data)
#j = 0

#while j<10:
    #print data[j]
    #print j
    #j = j+1

#print type(data)
#print type(data[0])
#print data[0]
#print len(data)
#print data[0]['Time']
    

    
