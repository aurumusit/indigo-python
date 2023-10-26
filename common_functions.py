# 1. Submolecule - 
# common_functions.py

import indigo

# Load a molecule from a Molfile
def load_molecule_from_file():
    indigo_instance = indigo.Indigo()
    return indigo_instance.loadMoleculeFromFile("sample_mol.mol")
    
# Create a submolecule from a list of atom indices
def create_submolecule(molecule, atom_indices):
    submolecule = molecule.createSubmolecule(atom_indices)
    return submolecule

# Create a submolecule from a list of atom indices and bond indices
def create_edge_submolecule(molecule, atom_indices, bond_indices):
    submolecule = molecule.createEdgeSubmolecule(atom_indices, bond_indices)
    return submolecule

# Get an atom by index
def get_atom(molecule, atom_index):
    return molecule.getAtom(atom_index)

# Get a bond by index
def get_bond(molecule, bond_index):
    return molecule.getBond(bond_index)

# Iterate over all atoms, including pseudoatoms and R-sites
def iterate_atoms(molecule):
    return molecule.iterateAtoms()

# Iterate over pseudoatoms
def iterate_pseudoatoms(molecule):
    return (atom for atom in molecule.iterateAtoms() if atom.isPseudo())

# Iterate over R-sites
def iterate_r_sites(molecule):
    return (atom for atom in molecule.iterateAtoms() if atom.isRSite())

# Iterate over bonds
def iterate_bonds(molecule):
    return molecule.iterateBonds()

# Add more functions as needed
