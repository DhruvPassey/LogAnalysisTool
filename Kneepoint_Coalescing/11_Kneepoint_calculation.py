#This script finds the final time window value by calculating the knee point of the graph and displays it to the user.
import subprocess
import os

os.chdir("C://Program Files//R//R-3.3.2//bin")

# Define command and arguments
command = 'Rscript.exe'
path2script = 'C:\Users\Dhruv_Passey_PC\Downloads\LogDiver\Final Log Analysis Tool\LogAnalysisTool\Kneepoint_Coalescing\Kneepoint.R'

threshhold = ['1000','10000']
k = 0

while k<len(threshhold):
    # Variable number of args in a list
    args = []
    args.append(threshhold[k])

    # Build subprocess command
    cmd = [command, path2script] + args

    # check_output will run the command and store to result
    x = subprocess.check_output(cmd, universal_newlines=True)

    print x

    k = k + 1

choice = (raw_input("Enter the threshhold value : "))

args = []
args.append(choice)

# Build subprocess command
cmd = [command, path2script] + args

# check_output will run the command and store to result
x = subprocess.check_output(cmd, universal_newlines=True)

print x
