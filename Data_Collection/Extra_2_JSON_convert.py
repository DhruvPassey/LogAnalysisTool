#This script converts all error logs extracted from splunk to JSON format
import json

with open("../Temp_Output/ErrorLogs.json") as f:
    content = f.readlines()

print content[0]

f3 = open("../Temp_Output/JSON_ErrorLogs2.json","a+")

i = len(content)
j = 0

while j<i:
    json_string = content[j]
    parsed_json = json.loads(json_string)
    #print type(parsed_json)
    #print parsed_json.items()
    json.dump(parsed_json,f3)
    j = j + 1

#Close the file
f3.close()

