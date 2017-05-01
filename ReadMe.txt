Steps to be followed for building this tool:

1) Install Python 2.7
	More details can be found at : https://www.python.org/download/releases/2.7/
	DO NOT use any version of python > 2.7

2) Install Splunk Enterprise (Latest Version)
	More details can be found at : https://www.splunk.com/
				       http://docs.splunk.com/Documentation/Splunk/6.5.3/Installation/InstallonWindows
	You are advised to download the most recent version of splunk-enterprise if a newer one exists.

3) Install Splunk SDK for Python (Latest Version)
	More details can be found at : http://dev.splunk.com/sdks
				       http://dev.splunk.com/view/python-sdk/SP-CAAAEDG
	You can use the sdk folder provided in the Data_Collection folder.(You are advised to download the most recent version of splunk-sdk for python if a newer one exists)

4) Install Elastic Search (Latest Version)
	More details can be found at : https://www.elastic.co/
				       https://www.elastic.co/guide/en/elasticsearch/reference/current/windows.html
	You can use the elastic search folder provided in the Data_Collection folder.(You are advised to download the most recent version of elasticsearch if a newer one exists)

5) Install R (Latest Version)
	More details can be found at : https://www.r-project.org/
				       https://cran.r-project.org/bin/windows/
	You are advised to download the most recent version of R if a newer one exists.

6) Install latest versions of python libraries as listed below:
	-NumPy
	-SciPy
	-Scikit Learn
	-GnuPlot
	
7) Install mhsmm package for R (Latest Version)
	More details can be found at : https://cran.r-project.org/web/packages/mhsmm/index.html

8) Please enter the complete path of all log files to be analysed in the file : Log Locations.txt

9) In file Kneepoint.R , in the first 2 lines , replace "C://Users//Dhruv_Passey_PC//Downloads//LogDiver//Final Log Analysis Tool//LogAnalysisTool//Temp_Output" with the actual path of the Temp_Output folder inside the folder you have just downloaded. (Instead of "/" use "//")

10) Repeat the above step for lines 49,50 and 54 of ModelFit.R

11) When you are finally ready just run the file : Master.py

NOTE : The Error prediction R script (ModelFit.r) contained an error so it has not been integrated with the rest of the tool. If you wish to see the problem please run it separately.
