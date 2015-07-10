#!/usr/bin/python

import os, subprocess

p = os.popen("find input -type d -name logs")

lines = p.readlines()

p.close()
#print lines

if os.path.exists("logs"):
    shutil.rmtree("logs")

os.mkdir("logs")

i=1

for line in lines :
    source=line.rstrip()
    destination="logs/logs"+str(i)
    subprocess.check_output(["cp", "-r", source, destination])
    i=i+1
    #print destination

     




