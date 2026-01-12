import os
import numpy as np


runs = ["RUN"+str(i+1) for i in range(25)]
wtimes = list()

wfile = open("TIMINGS.dat","w")
for run in runs:
    filename = os.path.join(run, "job.out")
    with open(filename,"r") as f:
        content = f.readlines()
    for line in content:
        if "seconds" in line:
            wtimes.append(eval(line.split()[-2]))

mean = np.mean(wtimes)
std  = np.std(wtimes)
for i, value in enumerate(wtimes):
    wfile.write(str(value)+"\n")

wfile.write("-----\n")
wfile.write("MEAN  "+str(round(mean,3))+"\n")
wfile.write("STD   "+str(round(std,3))+"\n")
wfile.close()
