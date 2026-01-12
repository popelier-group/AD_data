import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
from polus.trajectories.calculators import ComputeRMSD, getDistance, getDihedral
from polus.trajectories.readers import ReadXYZFile
from mpl_toolkits.axes_grid1 import make_axes_locatable


def compute_distance(geom,indices):
    atom1 = geom[indices[0]]
    atom2 = geom[indices[1]]
    return getDistance(atom1,atom2)

def compute_dihedral(geom,indices):
    atom1 = geom[indices[0]]
    atom2 = geom[indices[1]]
    atom3 = geom[indices[2]]
    atom4 = geom[indices[3]]
    return getDihedral(atom1,atom2,atom3,atom4)[1]

def load_geometries(xyz):
    return ReadXYZFile(xyz)

#fig,axs   = plt.subplots(1,3,figsize=(12,4))
#axs       = axs.flatten()
xyz_files = ["C5/OPT.xyz", "C7AX/OPT.xyz", "C7EQ/OPT.xyz"]
#disps     = ["Optimized", "Optimized", "Optimized"]
confs     = ["C5","C7Ax","C7Eq"]
PHI       = [5,4,3,1]
PSI       = [7,5,4,3]
ONON      = [2,3,6,7]
OO        = [2,6]
NN        = [3,7]
CC        = [0,8]
HH        = [13,15]
for i,xyz_file in enumerate(xyz_files):
    #ax   = axs[i]
    #disp = disps[i]
    conf  = confs[i]
    print("CONF  ", conf)
    geoms = load_geometries(xyz_file)
    keys  = [key for key in geoms.keys()]
    data      = {"phi":  list(),
                 "psi":  list(),
                 "onon": list(),
                 "oo":   list(),
                 "nn":   list(),
                 "cc":   list(),
                 "hh":   list()}
    for key in keys:
        geom  = geoms[key]
        phi   = compute_dihedral(geom,PHI)
        psi   = compute_dihedral(geom,PSI)
        onon  = compute_dihedral(geom,ONON)
        oo    = compute_distance(geom,OO)
        nn    = compute_distance(geom,NN)
        cc    = compute_distance(geom,CC)
        hh    = compute_distance(geom,HH)
        data["phi"].append(phi)
        data["psi"].append(psi)
        data["onon"].append(onon)
        data["oo"].append(oo)
        data["nn"].append(nn)
        data["cc"].append(cc)
        data["hh"].append(hh)

    stats =  dict()
    for key in data.keys():
        data_ = data[key]
        stats[key] = [np.mean(data_), np.std(data_)]
        print(f" {key.upper():<10}  {stats[key][0]:6.2f}  {stats[key][1]:6.2f}")
"""
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
"""
