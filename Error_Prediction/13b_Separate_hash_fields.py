#This script hashes each field of a log entry to an integer
import json
import time
from operator import itemgetter
from datetime import datetime
import matplotlib.pyplot as plt
import hashlib

with open("../Temp_Output/ErrorTuples.json") as f:
    errortuples = json.load(f)

with open("../Temp_Output/NonErrorTuples.json") as f:
    nonerrortuples = json.load(f)

f8 = open("../Temp_Output/ErrorTuplesLength.txt","a+")
f9 = open("../Temp_Output/NonErrorTuplesLength.txt","a+")

#print errortuples[0]

perrortuples = []
pnonerrortuples = []

i = 0

while i<len(errortuples):
    j = 0
    temp = []
    while j<len(errortuples[i]):
        dict = {'Time' : 0 , 'Date' : 0 , 'ProcessId' : 0 , 'ThreadId' : 0}
        if (errortuples[i][j].has_key('Time')):
            dict['Time'] = int(hashlib.sha1(errortuples[i][j]['Time']).hexdigest(), 16) % (10 ** 8)
        else:
            dict['Time'] = int(hashlib.sha1(errortuples[i][j]['_time']).hexdigest(), 16) % (10 ** 8)
        if (errortuples[i][j].has_key('Date')):
            dict['Date'] = int(hashlib.sha1(errortuples[i][j]['Date']).hexdigest(), 16) % (10 ** 8)
        else:
            dict['Date'] = 0
        if (errortuples[i][j].has_key('ProcessId')):
            dict['ProcessId'] = errortuples[i][j]['ProcessId']
        else:
            dict['ProcessId'] = 0
        if (errortuples[i][j].has_key('ThreadId')):
            dict['ThreadId'] = errortuples[i][j]['ThreadId']
        else:
            dict['ThreadId'] = 0
        temp.append(dict)
        j = j + 1
    perrortuples.append(temp)
    i = i + 1
        
#print perrortuples

i = 0

while i<len(nonerrortuples):
    j = 0
    temp = []
    while j<len(nonerrortuples[i]):
        dict = {'Time' : 0 , 'Date' : 0 , 'ProcessId' : 0 , 'ThreadId' : 0}
        if (nonerrortuples[i][j].has_key('Time')):
            dict['Time'] = int(hashlib.sha1(nonerrortuples[i][j]['Time']).hexdigest(), 16) % (10 ** 8)
        else:
            dict['Time'] = int(hashlib.sha1(nonerrortuples[i][j]['_time']).hexdigest(), 16) % (10 ** 8)
        if (nonerrortuples[i][j].has_key('Date')):
            dict['Date'] = int(hashlib.sha1(nonerrortuples[i][j]['Date']).hexdigest(), 16) % (10 ** 8)
        else:
            dict['Date'] = 0
        if (nonerrortuples[i][j].has_key('ProcessId')):
            dict['ProcessId'] = nonerrortuples[i][j]['ProcessId']
        else:
            dict['ProcessId'] = 0
        if (nonerrortuples[i][j].has_key('ThreadId')):
            dict['ThreadId'] = nonerrortuples[i][j]['ThreadId']
        else:
            dict['ThreadId'] = 0
        temp.append(dict)
        j = j + 1
    pnonerrortuples.append(temp)
    i = i + 1
        
#print pnonerrortuples

errortuplelength = []

out = open('../Temp_Output/ErrorTupleDataFinal.csv', 'a+')
i = 0
while i<len(perrortuples):
    j = 0
    errortuplelength.append(len(perrortuples[i]))
    while j<len(perrortuples[i])-1:
        out.write('%d,' % perrortuples[i][j]['Time'])
        out.write('%d,' % perrortuples[i][j]['Date'])
        out.write('%d,' % perrortuples[i][j]['ProcessId'])
        out.write('%d' % perrortuples[i][j]['ThreadId'])
        out.write('\n')
        j = j + 1
    i = i + 1
out.close()

print errortuplelength

nonerrortuplelength = []

out = open('../Temp_Output/NonErrorTupleDataFinal.csv', 'a+')
i = 0
while i<len(pnonerrortuples):
    j = 0
    nonerrortuplelength.append(len(pnonerrortuples[i]))
    while j<len(pnonerrortuples[i])-1:
        out.write('%d,' % pnonerrortuples[i][j]['Time'])
        out.write('%d,' % pnonerrortuples[i][j]['Date'])
        out.write('%d,' % pnonerrortuples[i][j]['ProcessId'])
        out.write('%d' % pnonerrortuples[i][j]['ThreadId'])
        out.write('\n')
        j = j + 1
    i = i + 1
out.close()

print nonerrortuplelength

i = 0
while i<len(errortuplelength)-1:
    f8.write(str(errortuplelength[i]))
    f8.write("\n")
    i = i + 1
f8.write(str(errortuplelength[i]))

i = 0
while i<len(nonerrortuplelength)-1:
    f9.write(str(nonerrortuplelength[i]))
    f9.write("\n")
    i = i + 1
f9.write(str(nonerrortuplelength[i]))

f8.close()
f9.close()
