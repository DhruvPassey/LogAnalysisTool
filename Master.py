import os

#Data Extraction
os.system("/Data_Collection/python 1_Common_format_Error_extraction.py")

os.system("/Data_Collection/python 2_3_JSON_convert_Extract_fields.py")

os.system("/Data_Collection/python 4_Common_format_Workloadlogs_extraction.py")

os.system("/Data_Collection/python 5_6_Workloadlogs_JSON_convert_Extract_fields.pyy")

f = open("../Temp_Output/Workload_Parsed_JSON_Logs_2.json","a+")
f.write(']')
f.close()

#elastic-search scripts
#os.system("python 7_ElasticSearch_load(optional).py")
#os.system("python 8_Elasticsearch_workload_consolidation(optional).py")
#os.system("python 8b_Elasticsearch_workload_consolidation(optional).py")

#Kneepoint Calculation and Coalescing
os.system("/Kneepoint_Coalescing/python 9_Sort_logs_timestamp.py")

#os.system("python Extra_10_Coalescing_varying_windows.py")

os.system("/Kneepoint_Coalescing/python 10_Coalescing_varying_windows_graph_plot.py")

os.system("/Kneepoint_Coalescing/python 11_Kneepoint_calculation.py")

os.system("/Kneepoint_Coalescing/python 12a_Preprocessing.py")

os.system("/Kneepoint_Coalescing/python 12b_Final_Coalescing.py")

#Error Prediction
os.system("/Error_Prediction/python 13a_Combined_single_hash.py")

os.system("/Error_Prediction/python 13b_Separate_hash_fields.py")




