#This script performs final coalescing using time window value specified by user
import json
import time
from operator import itemgetter
from datetime import datetime
import matplotlib.pyplot as plt

with open("../Temp_Output/Sorted_Workload_Parsed_JSON_Logs_2.json") as f:
    data = json.load(f)

f6 = open("../Temp_Output/ErrorTuples.json","a+")
f7 = open("../Temp_Output/NonErrorTuples.json","a+")

#print data[1]
#print type(data[1])

#W = float(raw_input("Enter the window size : "))
#W = 60.5605606
#W = 10
W = int(raw_input("Enter value of time window : "))

tuples = []
temp = []

curr = 0
next = curr + 1
no = 0
temp.append(data[curr])
while curr<len(data)-2:
    delta = datetime.strptime(data[next]['_time'],"%Y-%m-%d %H:%M:%S.%f India Standard Time") - datetime.strptime(data[curr]['_time'],"%Y-%m-%d %H:%M:%S.%f India Standard Time")
    if (delta.seconds<W):
        no = no+0
        #print next
        temp.append(data[next])
        curr = curr+1
        next = next+1
    else:
        no = no+1
        curr=next
        next = curr+1
        tuples.append(temp)
        temp = []
        temp.append(data[curr])

print no

with open("Error_Parsed_JSON_Logs_2.json") as f:
    errordata = json.load(f)

#print errordata[0]

errortime = []
i = 0

while i<len(errordata):
    errortime.append(errordata[i]['_time'])
    i = i + 1

#print errortime

L = 60
errortuples = []
nonerrortuples = []

i = 0
while i<len(tuples):
    j = len(tuples[i]) - 1
    k = 0
    a = 0
    while k<len(errortime):
        delta = (datetime.strptime(errortime[k],"%Y-%m-%d %H:%M:%S.%f India Standard Time") - datetime.strptime(tuples[i][j]['_time'],"%Y-%m-%d %H:%M:%S.%f India Standard Time"))
        if (delta.seconds <= L):
            errortuples.append(tuples[i])
            a = 1
            break;
        k = k + 1
    if (a == 0):
        nonerrortuples.append(tuples[i])
    i = i + 1

print errortuples[0]

##errortuples = []
##nonerrortuples = []
##
##i = 0
##while i<len(tuples):
##    j = 0
##    a = 0
##    while j<len(tuples[i]):
##        if (tuples[i][j] in errordata):
##            a = 1
##            errortuples.append(tuples[i])
##            break
##        j = j + 1
##    if (a == 0):
##        nonerrortuples.append(tuples[i])
##    i = i + 1
            
print len(errortuples)
print len(nonerrortuples)
#print errortuples[0]
#i = 0
#sum = 0
#while i<len(errortuples):
    #sum = sum + len(errortuples[i])
    #i = i + 1
#print sum

#i = 0
#sum = 0
#while i<len(nonerrortuples):
    #sum = sum + len(nonerrortuples[i])
    #i = i + 1
#print sum

i = 0
f6.write("[")
while i<len(errortuples)-1:
    json.dump(errortuples[i],f6)
    f6.write(",")
    i = i + 1
json.dump(errortuples[i],f6)
f6.write("]")

i = 0
f7.write("[")
while i<len(nonerrortuples)-1:
    json.dump(nonerrortuples[i],f7)
    f7.write(",")
    i = i + 1
json.dump(nonerrortuples[i],f7)
f7.write("]")

f6.close()
f7.close()
    





