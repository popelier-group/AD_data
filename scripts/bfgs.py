from ase.io import read,write,Trajectory
from ase.vibrations import Vibrations
from ase.optimize import BFGS
from fflux_calculator import FFLUX

# Define the atomic structure
atoms = read("ALANINE.xyz")

# Assign calculator 
atoms.calc = FFLUX(atoms=atoms)

# Run geometry optimization using BFGS algorithm
optimizer = BFGS(atoms, trajectory='opt.traj', logfile='opt.log')
optimizer.run(fmax=0.023)  # Stop when forces < 0.01 eV/Angstrom

# Save optimized geometry
write('ala_optimized.xyz', atoms)

# Print final energy and geometry
print("Final energy:", atoms.get_potential_energy())
print("Final positions:\n", atoms.get_positions())


# Write trajectory
traj_read = Trajectory(filename="opt.traj",mode="r",properties=["energy","forces"])
write(filename="opt_path.xyz",format="xyz", images=traj_read, append=True)

