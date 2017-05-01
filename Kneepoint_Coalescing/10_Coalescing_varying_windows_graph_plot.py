#This script performs coalescing using different time window values and different step values,plots a graph for each and then asks the user to select final values for the final graph
import json
import time
from operator import itemgetter
from datetime import datetime
import matplotlib.pyplot as plt

with open("../Temp_Output/Sorted_Workload_Parsed_JSON_Logs_2.json") as f:
    data = json.load(f)

step = [0.5,1,2,5]

f4 = open("../Temp_Output/TimeWindow.txt","a+")
#f4.write("[")

f5 = open("../Temp_Output/TimeStep.txt","a+")
#f5.write("[")

i = 0
graph = []
stept = []

for x in step:
    k = 0
    tempgraph = []
    tempstep = []

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
        tempgraph.append(no)
        tempstep.append(k)
        k = k+x

    graph.append(tempgraph)
    stept.append(tempstep)
    print graph[i]

    plt.plot(stept[i],graph[i], 'ro')
    plt.show()
    
    i = i+1
    
choice = float(raw_input("Enter the step value : "))

tempgraph = []
tempstep = []

k = 0

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
    tempgraph.append(no)
    tempstep.append(k)
    k = k+choice

print tempgraph

plt.plot(tempstep,tempgraph, 'ro')
plt.show()

k = 0
while k<251:
    f4.write(str(tempgraph[k]))
    f5.write(str(tempstep[k]))
    if (k<250):
        f4.write("\n")
        f5.write("\n")
    k = k+1

#f4.write("]")
f4.close()

#f5.write("]")
f5.close()


