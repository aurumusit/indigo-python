import indigo

# Initialize Indigo
indigo_instance = indigo.Indigo()

# Define the SMILES string of the chemical
smiles = "COC1C(C(C)=O)=C(OC)C=C(Br)C=1"  # Replace with your desired SMILES

# Convert SMILES to canonical SMILES using Indigo
mol = indigo_instance.loadMolecule(smiles)
can_smile = mol.canonicalSmiles()

# Print the canonical SMILES
print("Canonical SMILES:", can_smile)
