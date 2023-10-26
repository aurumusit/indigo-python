import indigo

# # Create an Indigo instance
indigo_instance = indigo.Indigo()

# # Load a molecule from a Molfile with aliases
# mol = indigo_instance.loadMolecule("OC([*:1])[*:2]")

# # Get the number of atoms before expansion
# num_atoms_before = mol.countAtoms()

# # Expand abbreviations
# mol.expandAbbreviations()

# # Get the number of atoms after expansion
# num_atoms_after = mol.countAtoms()

# if num_atoms_before == num_atoms_after:
#     print("No abbreviations were expanded.")
# else:
#     print("Abbreviations were successfully expanded.")

# ## Save Molecules

# import indigo

# # Create an Indigo instance
# indigo_instance = indigo.Indigo()

# # Load a molecule from a Molfile
# mol = indigo_instance.loadMolecule("CCO")

# # Save the molecule as a Molfile
# with open("output.mol", "w") as molfile:
#     molfile.write(mol.molfile())


# cml = mol.cml()

# # Save the molecule as a CML file
# with open("output.cml", "w") as cml_file:
#     cml_file.write(cml)


## Calculating Properties

# # Create an Indigo instance
# indigo_instance = indigo.Indigo()

# # Load a molecule from a Molfile
# mol = indigo_instance.loadMolecule("CC(=O)C1C(=CC(Br)=CC=1OC)OC")

# # Calculate the number of atoms
# num_atoms = mol.countAtoms()
# print(f"Number of atoms: {num_atoms}")

# num_pseudoatoms = mol.countPseudoatoms()
# print(f"Number of pseudoatoms: {num_pseudoatoms}")

# num_rsites = mol.countRSites()
# print(f"Number of R-sites: {num_rsites}")

# num_bonds = mol.countBonds()
# print(f"Number of bonds: {num_bonds}")


# formula = mol.grossFormula()
# print(f"Gross formula: {formula}")


# weight = mol.molecularWeight()
# print(f"Molecular weight: {weight} g/mol")

# abundant_mass = mol.mostAbundantMass()
# print(f"Most abundant isotopes mass: {abundant_mass} g/mol")


# monoisotopic = mol.monoisotopicMass()
# print(f"Monoisotopic mass: {monoisotopic} g/mol")


# has_coordinates = mol.hasCoord()
# print(f"Has coordinates: {has_coordinates}")

# has_3d_coordinates = mol.hasZCoord()
# print(f"Has 3D coordinates: {has_3d_coordinates}")


# is_chiral = mol.isChiral()
# print(f"Is chiral: {is_chiral}")


# heavy_atoms = mol.countHeavyAtoms()
# print(f"Number of heavy atoms (excluding hydrogens): {heavy_atoms}")

# implicit_hydrogens = mol.countImplicitHydrogens()
# print(f"Number of implicit hydrogens: {implicit_hydrogens}")



# total_hydrogens = mol.countHydrogens()
# print(f"Total number of hydrogens: {total_hydrogens}")

# sssr_count = mol.countSSSR()
# print(f"Number of SSSR cycles: {sssr_count}")


# Create an Indigo instance
# indigo_instance = indigo.Indigo()

# # Load a molecule with bad valence
# mol_with_bad_valence = indigo_instance.loadMolecule("CC(=O)[O]")

# # Check for bad valence
# valence_issues = mol_with_bad_valence.checkBadValence()

# if valence_issues:
#     print(f"Molecule has bad valence issues: {valence_issues}")
# else:
#     print("Molecule has correct valence.")


# # Load a molecule with ambiguous hydrogen positions
# mol_with_ambiguous_h = indigo_instance.loadMolecule("C(C)(C)(C)(C)(C)")

# # Check for ambiguous hydrogen positions
# h_position_issues = mol_with_ambiguous_h.checkAmbiguousH()

# if h_position_issues:
#     print(f"Molecule has ambiguous hydrogen positions: {h_position_issues}")
# else:
#     print("Molecule has unambiguous hydrogen positions.")

##connected components


# Load a molecule
mol = indigo_instance.loadMolecule("CCO.CC1=CC=CC=C1.CC(=O)O")

# Count the number of connected components
component_count = mol.countComponents()
print(f"{component_count} components")

# Iterate over the components
for comp in mol.iterateComponents():
    # Clone the component and print its SMILES representation
    print(comp.clone().smiles())
    
    # Print information about the component
    print(f"component {comp.index()}: {comp.countAtoms()} atoms, {comp.countBonds()} bonds")
    
    # Iterate over atoms in the component and print their indices
    for atom in comp.iterateAtoms():
        print(atom.index())

# Iterate over all atoms in the original molecule and print their component indices
for atom in mol.iterateAtoms():
    print(f"Atom {atom.index()} belongs to component {atom.componentIndex()}")

# Iterate over atoms in a specific component (component 0 in this example) and print their indices
for atom in mol.component(0).iterateAtoms():
    print(f"Atom {atom.index()} in component 0")