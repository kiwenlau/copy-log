#!/usr/bin/python

# copy logs of all benchmarks 
# input: the directory of benchmark result
# logs: save all logs

import os, subprocess


# get the path of all logs
p = os.popen("find input -type d -name logs")
lines = p.readlines()
p.close()

# create the directory for saving all logs
if os.path.exists("logs"):
    shutil.rmtree("logs")
os.mkdir("logs")

# copy all logs from benchmark result
i=1
for line in lines :
    source=line.rstrip()
    destination="logs/logs"+str(i)
    subprocess.check_output(["cp", "-r", source, destination])
    i=i+1