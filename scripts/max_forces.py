import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
from polus.trajectories.calculators import ComputeRMSD
from polus.trajectories.readers import ReadXYZFile
from mpl_toolkits.axes_grid1 import make_axes_locatable
from mpl_toolkits.axes_grid1.inset_locator import inset_axes


fig,axs = plt.subplots(1,3,figsize=(12,4))
axs = axs.flatten()
force_files = ["C5/MAX_FORCES.dat",
             "C7AX/MAX_FORCES.dat",
             "C7EQ/MAX_FORCES.dat"]
disps = ["Optimized", "Optimized", "Optimized"]
confs = ["C5","C7ax","C7eq"]

for i,force_file in enumerate(force_files):
    ax = axs[i]
    disp = disps[i]
    conf = confs[i]
    with open(force_file, "r") as f:
        content = f.readlines()
    ax.set_xlabel("Iteration")
    ax.set_ylabel("max force (kcal.mol$^{-1}\AA^{-1}$)")
    #ax.set_title("Optimization of "+conf+" structures")
    ax.set_title(conf,fontsize=16)
    #ax.grid()
    maxmax = 0.0
    minmax = 1000000.0
    for line in content:
        forces = [eval(x) for x in line.split(",")]
        iters  = [i for i in range(len(forces))]
        ax.plot(iters,forces,linewidth=1)
        maxmax_ = max(forces)
        minmax_ = min(forces)
        if maxmax_> maxmax:
            maxmax = maxmax_
        if minmax_< minmax:
            minmax = minmax_
    ax.text(len(iters)/2.5, 0.93*maxmax, str(round(maxmax,1)), fontsize=18, color="red")
    ax.text(len(iters)/2.1, 0.82*maxmax, str(round(minmax,1)), fontsize=18, color="blue")

    axins = inset_axes(
    ax,
    width="50%",   # relative to parent
    height="50%",
    loc="center",
    borderpad=1)

    for line in content:
        forces = [eval(x) for x in line.split(",")][:21]
        iters  = [i for i in range(len(forces))][:21]
        axins.plot(iters, forces)
        if i==0:
            yt = 600
        elif i==1:
            yt = 700
        else:
            yt = 500
        axins.text(5,yt,"25 runs", fontsize=16)
    #axins.set_title("First 20 iterations", fontsize=8)

    #axins.tick_params(labelsize=6)
    #axins.spines["top"].set_visible(False)
    #axins.spines["right"].set_visible(False)
    #ax.text(30,600,"25 runs", fontsize=16)

plt.tight_layout()
plt.savefig("max_forces_all_confs.png",dpi=300)
plt.show()
