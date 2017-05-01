#This script performs coalescing using different time windows increasing in steps of 1s
import json
import time
from operator import itemgetter
from datetime import datetime

with open("../Temp_Output/Sorted_Workload_Parsed_JSON_Logs_2.json") as f:
    data = json.load(f)

f4 = open("../Temp_Output/TimeWindow.txt","a+")
f4.write("[")

k = 0
graph = []

while k<251:
    curr = 0
    next = curr+1
    no = 1
    W = k
    while curr<len(data)-1:
        delta = datetime.strptime(data[next]['_time'],"%Y-%m-%d %H:%M:%S.%f India Standard Time") - datetime.strptime(data[curr]['_time'],"%Y-%m-%d %H:%M:%S.%f India Standard Time")
        if (delta.seconds<W):
            no = no+0
            curr = curr+1
            next = next+1
        else:
            no = no+1
            curr=next
            next = curr+1
    print no
    graph.append(no)
    k = k+1

print graph

k = 0

while k<251:
    f4.write(str(graph[k]))
    if (k<250):
        f4.write(",")
    k = k+1

f4.write("]")
f4.close()
