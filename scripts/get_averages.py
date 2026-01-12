import os
import numpy as np


confs = ["C5","C7AX","C7EQ"]
files = [conf+"-0.25-TIMINGS-ENERGIES.txt" for conf in confs]
energies = dict()
times    = dict()
for i,file in enumerate(files):
    with open(file,"r") as f:
        content = f.readlines()
    en = list()
    t  = list()
    count = 0
    for line in content:
        line = line.split(",")
        if line[1] != " None":
            en_ = eval(line[1])
            if en_ < -496.0:
                en.append(eval(line[1]))
                t.append(eval(line[2]))
                count +=1 
    av_e, std_e = np.mean(en), np.std(en)
    av_t, std_t = np.mean(t),  np.std(t)
    ci_e, ci_t  = 1.96*std_e/np.sqrt(count), 1.96*std_t/np.sqrt(count)
    print(f" CONF {confs[i]:8}  AV/E {av_e:10.6f}  STD_E {std_e:10.4f}  CI {ci_e:10.4f}  N {count:4}")
    print(f" CONF {confs[i]:8}  AV/T {av_t:10.6f}  STD_T {std_t:10.4f}  CI {ci_t:10.4f}  N {count:4}") 
