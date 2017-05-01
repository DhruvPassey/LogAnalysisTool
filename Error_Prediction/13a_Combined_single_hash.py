#This script hashes an entire log entry into a single integer
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

f8 = open("../Temp_Output/HashedErrorTuplesLength.txt","a+")
f9 = open("../Temp_Output/HashedNonErrorTuplesLength.txt","a+")

#print errortuples[0]

hashederrortuples = []
hashednonerrortuples = []

i = 0

while i<len(errortuples):
    j = 0
    temp = []
    #print len(errortuples[i])
    while j<len(errortuples[i]):
        #print str(i) + ' ' + str(j)
        if (errortuples[i][j].has_key('Time')):
            w = errortuples[i][j]['Time']
        else:
            w = errortuples[i][j]['_time']
        if (errortuples[i][j].has_key('Date')):
            x = errortuples[i][j]['Date']
        else:
            x = str(0)
        if (errortuples[i][j].has_key('ProcessId')):
            y = str(errortuples[i][j]['ProcessId'])
        else:
            y = str(0)
        if (errortuples[i][j].has_key('ThreadId')):
            z = str(errortuples[i][j]['ThreadId'])
        else:
            z = str(0)
        a = w + ';' + x + ';' + y + ';' + z
        hashcode = int(hashlib.sha1(a).hexdigest(), 16) % (10 ** 8)
        temp.append(hashcode)
        j = j + 1
    hashederrortuples.append(temp)
    i = i + 1

#print hashederrortuples

while i<len(nonerrortuples):
    j = 0
    temp = []
    #print len(nonerrortuples[i])
    while j<len(nonerrortuples[i]):
        #print str(i) + ' ' + str(j)
        if (nonerrortuples[i][j].has_key('Time')):
            w = nonerrortuples[i][j]['Time']
        else:
            w = nonerrortuples[i][j]['_time']
        if (nonerrortuples[i][j].has_key('Date')):
            x = nonerrortuples[i][j]['Date']
        else:
            x = str(0)
        if (nonerrortuples[i][j].has_key('ProcessId')):
            y = str(nonerrortuples[i][j]['ProcessId'])
        else:
            y = str(0)
        if (nonerrortuples[i][j].has_key('ThreadId')):
            z = str(nonerrortuples[i][j]['ThreadId'])
        else:
            z = str(0)
        a = w + ';' + x + ';' + y + ';' + z
        hashcode = int(hashlib.sha1(a).hexdigest(), 16) % (10 ** 8)
        temp.append(hashcode)
        j = j + 1
    hashednonerrortuples.append(temp)
    i = i + 1

#print hashednonerrortuples

errortuplelength = []

out = open('HashedErrorTupleDataFinal.txt', 'a+')
i = 0
while i<len(hashederrortuples):
    j = 0
    errortuplelength.append(len(hashederrortuples[i]))
    while j<len(hashederrortuples[i])-1:
        out.write('%d' % hashederrortuples[i][j])
        out.write('\n')
        j = j + 1
    i = i + 1
out.close()

print errortuplelength

nonerrortuplelength = []

out = open('HashedNonErrorTupleDataFinal.txt', 'a+')
i = 0
while i<len(hashednonerrortuples):
    j = 0
    nonerrortuplelength.append(len(hashednonerrortuples[i]))
    while j<len(hashednonerrortuples[i])-1:
        out.write('%d' % hashednonerrortuples[i][j])
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
        


