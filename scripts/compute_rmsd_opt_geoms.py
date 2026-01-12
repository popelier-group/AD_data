import os
import numpy as np
import matplotlib.pyplot as plt
from polus.trajectories.calculators import ComputeRMSD
from polus.trajectories.readers import ReadXYZFile


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


if __name__=="__main__":
    xyz_file = "OPT.xyz"
    ref_geom   = load_geometries("ALANINE_C5.xyz")[0]
    test_geoms = load_geometries(xyz_file)
    max_rmsd    = 0.0
    max_rmsd_   = 0.0
    min_rmsd    = 100000.0
    min_rmsd_   = 100000.0
    rmsds_all   = list()
    rmsds_heavy= list()
    for key in test_geoms.keys():
        test_geom = test_geoms[key]
        rmsd      = compute_rmsd_all_atoms(ref_geom,test_geom)
        rmsd_     = compute_rmsd_heavy_atoms(ref_geom,test_geom)
        rmsds_all.append(rmsd)
        rmsds_heavy.append(rmsd_)
        print(f"Geom {key:6}  RMSD_ALL  {rmsd:10.4f}  RMSD_HEAVY {rmsd_:10.4f}  ")
        if rmsd > max_rmsd:
            max_rmsd = rmsd
        if rmsd_ > max_rmsd_:
            max_rmsd_ = rmsd_
        if rmsd < min_rmsd:
            min_rmsd = rmsd
        if rmsd_ < min_rmsd_:
            min_rmsd_ = rmsd_
    print(f"MIN_RMSD_ALL {min_rmsd:6.2f}  MAX_RMSD_ALL {max_rmsd:6.3f}  MIN_RMSD_HEAVY {min_rmsd_:6.2f}  MAX_RMSD_HEAVY {max_rmsd_:6.2f}")

mean, mean_ = np.mean(rmsds_all), np.mean(rmsds_heavy)
std, std_   = np.std(rmsds_all), np.std(rmsds_heavy)
print(f"MEAN/ALL {mean:6.3f}  STD/ALL {std:6.3f}  CI {1.96*std/5.0:6.3f}")
print(f"MEAN/HVY {mean_:6.3f}  STD/HVY {std_:6.3f}  CI {1.96*std_/5.0:6.3f}")
fig,ax = plt.subplots(1,1, figsize=(4,4))
x = [i for i in range(len(rmsds_all))]

ax.plot(x,rmsds_all, color="blue", linewidth=2, label="ALL")
ax.plot(x,rmsds_heavy, color="red", linewidth=2, label="HEAVY")
ax.set_xlabel("Iteration")
ax.set_ylabel("RMSD ($\AA$)")
ax.legend()
plt.tight_layout()
plt.show()
