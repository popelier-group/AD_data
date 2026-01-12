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
energy_files = ["C5/ENERGY_PATH.dat",
             "C7AX/ENERGY_PATH.dat",
             "C7EQ/ENERGY_PATH.dat"]
disps = ["Optimized", "Optimized", "Optimized"]
confs = ["C5","C7ax","C7eq"]
ref_energies = [-496.060960, -496.058348, -496.062313]

for i,energy_file in enumerate(energy_files):
    ax = axs[i]
    disp = disps[i]
    conf = confs[i]
    ref  = ref_energies[i]
    with open(energy_file, "r") as f:
        content = f.readlines()
    ax.set_xlabel("Iteration")
    ax.set_ylabel("Potential energy (Hartree)")
    ax.set_title(conf)
    maxe = -10000000000.0
    for line in content:
        line = line[1:]
        energies = [eval(x) for x in line.split(",")]
        iters  = [i for i in range(len(energies))]
        ax.plot(iters,energies,linewidth=2)
        maxe_ = max(energies)
        if maxe_> maxe:
            maxe = maxe_
    ax.text(len(iters)/3.5, maxe-0.1, str(round(maxe,6)), fontsize=16, color="red")
    ax.axhline(ref,linestyle="--")

    axins = inset_axes(
    ax,
    width="60%",   # relative to parent
    height="50%",
    loc="center right",
    borderpad=1)

    for line in content:
        line = line[1:]
        energies = [eval(x) for x in line.split(",")][:21]
        iters  = [i for i in range(len(energies))][:21]
        axins.plot(iters, energies)
    #axins.set_title("First 20 iterations", fontsize=8)

    #axins.tick_params(labelsize=6)
    #axins.spines["top"].set_visible(False)
    #axins.spines["right"].set_visible(False)

plt.tight_layout()
plt.savefig("opt_energies_all_confs.png",dpi=300)
plt.show()
