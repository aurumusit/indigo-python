# Import the functions from common_functions.py
from common_functions import *


molecule = load_molecule_from_file()
print("Loaded molecule from file:")
print(molecule.smiles())

atom_indices = [1, 2, 3]  # You can provide the desired atom indices
submolecule = create_submolecule(molecule, atom_indices)
print("\nSubmolecule created from specific atoms:")
print(submolecule.smiles())
