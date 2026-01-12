import os
import numpy as np


runs = ["RUN"+str(i+1) for i in range(25)]

optfile = open("OPT.xyz","w")
for k,run in enumerate(runs):
    filename = os.path.join(run, "ala_optimized.xyz")
    with open(filename,"r") as f:
        content = f.readlines()
    for i,line in enumerate(content):
        if i==0:
            line = line
        if i==1:
            line = "OPT-geom-"+str(k+1)+"\n"
        else:
            line = "    ".join(line.split()[:4])+"\n"
        optfile.write(line)
optfile.close()
