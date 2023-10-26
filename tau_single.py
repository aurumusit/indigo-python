import indigo

# Initialize Indigo
indigo_instance = indigo.Indigo()

# Define the SMILES string of the chemical
smiles = "CC(=O)C"  # Replace with your desired SMILES

# Convert SMILES to canonical SMILES using Indigo
mol = indigo_instance.loadMolecule(smiles)
can_smile = mol.canonicalSmiles()

# Print the canonical SMILES
print("Canonical SMILES:", smiles)

# Print the list of tautomers for the molecule
tautomers = indigo_instance.iterateTautomers(mol, 'INCHI')
print(f'Tautomers: {tautomers}')
#Create a list to store tautomers' SMILES
tautomer_smiles = []
# tau = molecule.clone()
# print(tau)

tau = mol.canonicalSmiles()
print(tau)
#Iterate through tautomers and add their canonical SMILES to the list
for index, tautomer in enumerate(tautomers):
    
    tautomer_smiles.append(mol.canonicalSmiles())
    print(f'Tautomer {index + 1}: {mol.canonicalSmiles()}')

# You can use the tautomer SMILES list for further processing
