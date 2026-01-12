import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
from polus.trajectories.calculators import ComputeRMSD
from polus.trajectories.readers import ReadXYZFile
from mpl_toolkits.axes_grid1 import make_axes_locatable


def compute_rmsd_all_atoms(geom1,geom2,natoms=22):
    weights = [1.0]*natoms
    rotmeth = "K"
    rmsd    = ComputeRMSD(geom1,geom2,rotmeth, False,weights)
    return rmsd

def compute_rmsd_heavy_atoms(geom1,geom2,natoms=22):
    weights = [1.0]*natoms
    for i in range(10,22):
        weights[i] = 0.0
    rotmeth = "K"
    rmsd    = ComputeRMSD(geom1,geom2,rotmeth, False,weights)
    return rmsd

def load_geometries(xyz):
    return ReadXYZFile(xyz)

fig,axs = plt.subplots(3,1,figsize=(5,12))
axs = axs.flatten()
energy_files = ["C5/ENERGIES.dat",
             "C7AX/ENERGIES.dat",
             "C7EQ/ENERGIES.dat"]
disps = ["Optimized", "Optimized", "Optimized"]
confs = ["C5","C7ax","C7eq"]
means = ["-496.060857","-496.058338","-496.062003"]
stds  = ["   0.000050","   0.000074","   0.000046"]

for i,energy_file in enumerate(energy_files):
    mean = means[i]
    std  = stds[i]
    ax = axs[i]
    disp = disps[i]
    conf = confs[i]
    #ref = -496.062310734
    energies_    = list()
    #max_diff = 0.0
    with open(energy_file,"r") as f:
        content = f.readlines()
    for line in content[:25]:
        line = line.replace("\n","")
        en   = eval(line)
        #diff = abs(en - ref)
        #if diff > max_diff:
        #    max_diff = diff
        energies_.append(en)

    #print(f"Maximum diff {max_diff*627.5: 7.2f}")
    energies = list()
    for i,en1 in enumerate(energies_):
        energies.append([])
        for j,en2 in enumerate(energies_):
            diff = abs(627.5*(en1 - en2))
            energies[i].append(diff)

    data = np.array(energies)
    mask = np.triu(np.ones_like(data, dtype=bool), k=0)
    masked_data = np.ma.array(data, mask=mask)

    im = ax.imshow(masked_data,cmap="magma")
    #im = ax.imshow(masked_data,cmap="winter")
    divider = make_axes_locatable(ax)
    cax = divider.append_axes("right", size="5%", pad=0.10)

    cbar = fig.colorbar(im, cax=cax, label="Relative energy (kcal/mol)")

    #cbar = fig.colorbar(im, ax=ax, label="Relative energy (kcal/mol)")
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.set_xlabel("Geometry ID")
    ax.set_ylabel("Geometry ID")
    #ax.set_title("Opt.  "+conf+"", fontsize=18)
    ax.text(9.5,6, mean, color="red", fontsize=15)
    ax.text(11,10, std, color="blue", fontsize=15)
    #ax.hlines(y=4, xmin=10, xmax=20, colors='black')
    #ax.hlines(y=12, xmin=10, xmax=20, colors='black')
    #cbar.formatter = ticker.FormatStrFormatter('%.2f')  # 2 decimals
    #cbar.update_ticks()
    cbar.formatter = ticker.ScalarFormatter(useMathText=True)
    cbar.formatter.set_powerlimits((0, 0))  # always use scientific notation
    cbar.update_ticks()

plt.tight_layout()
plt.savefig("relative_energies_all_confs_opt_vertical.png",dpi=300)
plt.show()
