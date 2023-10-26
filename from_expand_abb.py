# import indigo

# # Create an Indigo instance
# indigo_instance = indigo.Indigo()

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












