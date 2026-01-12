import os
import numpy as np


runs = ["RUN"+str(i+1) for i in range(25)]
energies = list()

wfile = open("ENERGIES.dat","w")
for run in runs:
    filename = os.path.join(run, "FFLUX.out")
    with open(filename,"r") as f:
        content = f.readlines()
    for line in content:
        line = line.split()
        if len(line)==1:
            temp =  eval(line[0])
    energies.append(temp)

mean = np.mean(energies)
std  = np.std(energies)
for i, value in enumerate(energies):
    wfile.write(str(value)+"\n")

wfile.write("-----\n")
wfile.write("MEAN  "+str(round(mean,6))+"\n")
wfile.write("STD   "+str(round(std,6))+"\n")
wfile.close()
