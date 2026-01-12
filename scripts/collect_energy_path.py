import os
import numpy as np


runs = ["RUN"+str(i+1) for i in range(25)]

efile = open("ENERGY_PATH.dat","w")
for k,run in enumerate(runs):
    filename = os.path.join(run, "FFLUX.out")
    with open(filename,"r") as f:
        content = f.readlines()[1:]
    for i,line in enumerate(content):
        line = line.split()
        if len(line)==1:
            e = eval(line[0])   
            if i==0:
               efile.write(str(e))
            else:
               efile.write(","+str(e))
    efile.write("\n")

efile.close()
