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

fig,axs = plt.subplots(1,3,figsize=(12,4))
axs = axs.flatten()
xyz_files = ["C5/OPT.xyz",
             "C7AX/OPT.xyz",
             "C7EQ/OPT.xyz"]
             #"alanine-langevin-displaced-0.4.xyz"]
disps = ["Optimized", "Optimized", "Optimized"]
confs = ["C5","C7Ax","C7Eq"]
for i,xyz_file in enumerate(xyz_files):
    ax = axs[i]
    disp = disps[i]
    conf = confs[i]
    test_geoms = load_geometries(xyz_file)
    keys     = [key for key in test_geoms.keys()]
    rmsds    = list()
    for i,key1 in enumerate(keys):
        rmsds.append([])
        geom1 = test_geoms[key1]
        for j,key2 in enumerate(keys):
            geom2 = test_geoms[key2]
            #rmsd      = compute_rmsd_all_atoms(geom1, geom2)
            rmsd      = compute_rmsd_heavy_atoms(geom1, geom2)
            rmsds[i].append(rmsd)

    data = np.array(rmsds)
    mask = np.triu(np.ones_like(data, dtype=bool), k=0)
    masked_data = np.ma.array(data, mask=mask)

    im = ax.imshow(masked_data)
    divider = make_axes_locatable(ax)
    cax = divider.append_axes("right", size="5%", pad=0.10)

    #fig.colorbar(im, ax=ax, label="RMSD ($\AA$)")
    cbar = fig.colorbar(im, cax=cax, label="RMSD ($\AA$)")
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.set_xlabel("Geometry ID")
    ax.set_ylabel("Geometry ID")
    ax.set_title("Opt. "+conf+" / Heavy atoms")

plt.tight_layout()
plt.savefig("relative_rmsds_all_confs_opt_heavy_atoms.png",dpi=300)
plt.show()
