import os
import numpy as np


runs = ["RUN"+str(i+1) for i in range(25)]

optfile = open("OPT.xyz","w")
mffile = open("MAX_FORCES.dat","w")
for k,run in enumerate(runs):
    filename = os.path.join(run, "opt.log")
    with open(filename,"r") as f:
        content = f.readlines()[1:]
    for i,line in enumerate(content):
        line = line.split()
        #mf =0.0194469*eval(line[-1])  #  Hartree/Bohr
        mf = 23.0605*eval(line[-1])   # kcal/mol/A
        if (i+1)!=len(content):
            mffile.write(str(mf)+",")
        else:
            mffile.write(str(mf))
    mffile.write("\n")

mffile.close()
