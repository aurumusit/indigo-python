##Import the functions from common_functions.py
from common_functions import *



##try running all the functions seperately for understanding


## Accessing Atoms and Bonds

molecule = load_molecule_from_file()
print("Loaded molecule from file:")
print(molecule.smiles())

atom_indices = [1, 2, 3]  # You can provide the desired atom indices
submolecule = create_submolecule(molecule, atom_indices)
print("\nSubmolecule created from specific atoms:")
print(submolecule.smiles())


# atom_indices = [1, 2, 3]
# bond_indices = [1, 2, 3]  # You can provide the desired atom and bond indices
# edge_submolecule = create_edge_submolecule(molecule, atom_indices, bond_indices)
# print("\nEdge submolecule created from specific atoms and bonds:")
# print(edge_submolecule.smiles())

atom_index = 2  # Replace with the desired atom index
atom = get_atom(molecule, atom_index)
print("\nAtom retrieved by index:")
print(atom.symbol())

bond_index = 7  # Replace with the desired bond index
bond = get_bond(molecule, bond_index)
print("\nBond retrieved by index:")
print(bond.bondOrder())

bond_index = 1  # Replace with the desired bond index
bond = get_bond(molecule, bond_index)
print("\nBond retrieved by index:")
print(bond.bondOrder())

print("\nIterating over all atoms:")
for atom in iterate_atoms(molecule):
    print(f"Atom: {atom.index()}, Symbol: {atom.symbol()}")

# print("\nIterating over pseudoatoms:")
# for atom in iterate_pseudoatoms(molecule):
#     print(atom)

print("\nIterating over bonds:")
for bond in iterate_bonds(molecule):
    print(f"Bond: {bond.index()}, Order: {bond.bondOrder()}")


## Properties of Atoms and Bonds
atom_index = 3

atom = get_atom(molecule, 3)
atomic_number = atom.atomicNumber()
print(f"Atomic Number: {atomic_number}")

atom = get_atom(molecule, atom_index)
isotope = atom.isotope()
print(f"Isotope: {isotope}")

atom = get_atom(molecule, atom_index)
degree = atom.degree()
print(f"Degree: {degree}")

charge = atom.charge()
print(f"Charge: {charge}")

explicit_valence = atom.getExplicitValence()
print(f"Explicit Valence: {explicit_valence}")

radical_electrons = atom.radicalElectrons()
print(f"Radical Electrons: {radical_electrons}")

hydrogen_count = atom.countHydrogens()
print(f"Total Hydrogens: {hydrogen_count}")

implicit_hydrogen_count = atom.countImplicitHydrogens()
print(f"Implicit Hydrogens: {implicit_hydrogen_count}")

valence = atom.valence()
print(f"Valence: {valence}")

is_pseudoatom = atom.isPseudoatom()
print(f"Is Pseudoatom: {is_pseudoatom}")

is_rsite = atom.isRSite()
print(f"Is R-Site: {is_rsite}")

atom_symbol = atom.symbol()
print(f"Atom Symbol: {atom_symbol}")

xyz_coordinates = atom.xyz()
print(f"XYZ Coordinates: {xyz_coordinates}")

# Check if the atom is an R-site before using getRSiteBits
atom = molecule.iterateAtoms().next()
if atom.isRSite():
    rsite_bits = atom.getRSiteBits()
    print(f"R-Site Bits: {rsite_bits}")
else:
    print("This is not an R-site atom.")

## Methods for Molecule's Bonds:

bond_index = 3

bond = get_bond(molecule, bond_index)
bond_order = bond.bondOrder()
print(f"Bond Order: {bond_order}")

source_atom = bond.source()
print(f"Source Atom: {source_atom.index()}")

destination_atom = bond.destination()
print(f"Destination Atom: {destination_atom.index()}")

bond = get_bond(molecule, bond_index)
topology = bond.topology()
print(f"Bond Topology: {topology}")


# Modifying Atoms and Bonds

atom = molecule.getAtom(0)

# Save the initial charge
initial_charge = atom.charge()

# Reset the charge of the atom
atom.resetCharge()

# Print the changes
print(f"Atom {atom.index()}: Charge reset from {initial_charge} to {atom.charge()}")

# Get an atom by index
atom = molecule.getAtom(1)

# Save the initial explicit valence
initial_valence = atom.getExplicitValence()

# Reset the explicit valence of the atom
atom.resetExplicitValence()

# Print the changes
print(f"Atom {atom.index()}: Explicit valence reset from {initial_valence} to {atom.getExplicitValence()}")

# Get an atom by index
atom = molecule.getAtom(2)

# Save the initial isotope value
initial_isotope = atom.isotope()

# Reset the isotope value of the atom
atom.resetIsotope()

# Print the changes
print(f"Atom {atom.index()}: Isotope value reset from {initial_isotope} to {atom.isotope()}")

# Save the initial radical electrons
initial_radical = atom.radicalElectrons()

# Reset the radical information of the atom
atom.resetRadical()


# Get an atom by index
atom = molecule.getAtom(4)

# Save the initial charge
initial_charge = atom.charge()

# Set the charge of the atom to +1
atom.setCharge(1)


# Print the changes
print(f"Atom {atom.index()}: Charge set from {initial_charge} to {atom.charge()}")

atom.resetCharge()

# Get an atom by index
atom = molecule.getAtom(5)

# Save the initial isotope value
initial_isotope = atom.isotope()

# Set the isotope of the atom to 13
atom.setIsotope(13)

# Print the changes
print(f"Atom {atom.index()}: Isotope set from {initial_isotope} to {atom.isotope()}")


# Get an atom by index
atom = molecule.getAtom(6)

# Save the initial XYZ coordinates
initial_xyz = atom.xyz()

# Set the XYZ coordinates of the atom
atom.setXYZ(1.0, 2.0, 3.0)



# Print the changes
print(f"Atom {atom.index()}: XYZ coordinates set from {initial_xyz} to {atom.xyz()}")

# Get an atom by index
atom = molecule.getAtom(7)

# Print the changes
print(f"Atom {atom.index()}: Attachment point set to {atom.setAttachmentPoint(2)}")




## Accessing Neighbor Atoms
for atom in molecule.iterateAtoms():
    print(f"atom {atom.index()}: {atom.degree()} neighbors")
    for neighbor in atom.iterateNeighbors():
        print(f"neighbor atom {neighbor.index()} is connected by bond {neighbor.bond().index()}")


# Iterate over R-groups in the query molecule
## Accessing R-Groups
indigo_instance = indigo.Indigo()

query_molecule = indigo_instance.loadQueryMolecule("C1=CC=CN=C1")
for rgroup in query_molecule.iterateRGroups():
    print(f"RGROUP #{rgroup.index()}")

    # Iterate over fragments within the R-group
    for fragment in rgroup.iterateRGroupFragments():
        print(f"  FRAGMENT #{fragment.index()}")
        print(fragment.molfile())
