import indigo

# Initialize Indigo
indigo_instance = indigo.Indigo()

# Load a molecule with chiral atoms from a Molfile
mol = indigo_instance.loadMoleculeFromFile("sample_mol.mol")

# Count and access chiral atoms
print(f"{mol.countStereocenters()} chiral atoms")
for atom in mol.iterateStereocenters():
    print(f"atom {atom.index()} -- stereocenter type {atom.stereocenterType()}")
    atom.invertStereo()

# Access and print bond stereo types
for bond in mol.iterateBonds():
    if bond.bondStereo() != 0:
        print(f"bond {bond.index()} -- stereo type {bond.bondStereo()}")

# Print the SMILES notation of the molecule
print(mol.smiles())

# Clear stereocenters and cis-trans configurations
mol.clearStereocenters()
mol.clearCisTrans()

# Print the SMILES notation after clearing
print(mol.smiles())
