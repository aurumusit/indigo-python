import pandas as pd
import indigo

# Initialize Indigo
indigo_instance = indigo.Indigo()

# Define a function to generate canonical SMILES
def generate_canonical_smiles(smiles):
    mol = indigo_instance.loadMolecule(smiles)
    can_smiles = mol.canonicalSmiles()
    return can_smiles

# Read the input file with ID and SMILES
input_file = "csv/smiles_1000.csv"  # Replace with your input file name
output_file = "excel/converted_smiles_1000.xlsx"  # Replace with your desired output file name

data = pd.read_csv(input_file)

# Apply the function to generate can_smiles
data["can_smiles"] = data["smile"].apply(generate_canonical_smiles)

# Store the results in an Excel file
data.to_excel(output_file, index=False, engine="openpyxl")

print("Canonical SMILES generated and stored in", output_file)
