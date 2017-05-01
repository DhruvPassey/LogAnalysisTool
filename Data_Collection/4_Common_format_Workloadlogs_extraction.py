#This script converts all log files to a common format and then extracts workload logs using Splunk.
import subprocess
import splunklib.client as client
import splunklib.results as results
import os
import platform
import json

with open("LogLocations.txt") as f:
    content = f.readlines()
try:
    f2 = open("../Temp_Output/Workload_Logs.json","a+")
    f3 = open("../Temp_Output/Workload_Clustering.txt","a+")

    HOST = "localhost"
    PORT = 8089
    #USERNAME = "admin"
    #PASSWORD = "Asia1996"
    USERNAME = str(raw_input("Enter Splunk Username : "))
    PASSWORD = str(raw_input("Enter Splunk Password : "))

    # Create a Service instance and log in 
    service = client.connect(
        host=HOST,
        port=PORT,
        username=USERNAME,
        password=PASSWORD)

    # Print installed apps to the console to verify login
    for app in service.apps:
        print app.name

    # Create a new index
    mynewindex = service.indexes.create("index_test")

    i = len(content)
    j = 0

    osName = platform.system()
    print osName

    while j<i:
        str = content[j]
        scontent = str.split("\\")
        name = scontent[len(scontent)-1]
        ext = name.split(".")
        fext = ext[len(ext)-1]
        if (fext=="evtx"):
            #print str
            #print ext
            command = "wevtutil qe /lf "+str+" > "+str[:-5]+"_converted.xml"  
            print subprocess.Popen(command, shell=True, stdout=subprocess.PIPE).stdout.read()
            # Create a oneshot input
            # Retrieve the index for the data
            myindex = service.indexes["index_test"]
            # Create a variable with the path and filename
            uploadme = str[:-5]+"_converted.xml"
            print uploadme
            # Upload and index the file
            myindex.upload(uploadme);

            # Run an export search and display the results using the results reader.
            # Set the parameters for the search:
            kwargs_export = {"search_mode": "normal","output_mode":"json"}
            searchquery_export = "search index=index_test"

            exportsearch_results = service.jobs.export(searchquery_export, **kwargs_export)
            f2.write(exportsearch_results.read())
            
            # Clean all events from the index
            #timeout = 60
            #myindex.clean(timeout)
        else:
            # Create a oneshot input
            # Retrieve the index for the data
            myindex = service.indexes["index_test"]
            # Create a variable with the path and filename
            uploadme = str[:-1]
            print uploadme
            # Upload and index the file
            myindex.upload(uploadme);

            # Run an export search and display the results using the results reader.
            # Set the parameters for the search:
            kwargs_export = {"search_mode": "normal","output_mode":"raw"}
            searchquery_export = "search index=index_test"

            exportsearch_results = service.jobs.export(searchquery_export, **kwargs_export)
            f3.write(exportsearch_results.read())
            
            kwargs_export_2 = {"search_mode": "normal","output_mode":"json"}
            searchquery_export_2 = "search index=index_test"

            exportsearch_results_2 = service.jobs.export(searchquery_export_2, **kwargs_export_2)
            f2.write(exportsearch_results_2.read())

            # Clean all events from the index and display its size again
            #timeout = 60
            #myindex.clean(timeout)
        j = j + 1

    #Delete the given index
    service.indexes.delete("index_test")
    print "...deleted!\n"
finally:
    #Close error logs file and clustering file
    f2.close()
    f3.close()
