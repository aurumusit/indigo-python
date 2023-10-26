import indigo
import pandas as pd

# Initialize Indigo
indigo_instance = indigo.Indigo()

# Process the new dataset
new_dataset_file = "csv/new_dataset.csv"
valid_tautomers_data = []

with open(new_dataset_file, "r") as new_file:
    next(new_file)  # Skip the header line
    for line in new_file:
        parts = line.strip().split(",")
        if len(parts) == 2:
            id, smile = parts[0], parts[1]
            # Check if the SMILES string is valid and size is less than or equal to 15
            if len(smile) <= 15:
                mol = indigo_instance.loadMolecule(smile)
                if mol:
                    try:
                        # Perform tautomer enumeration for valid SMILES
                        tautomers = indigo_instance.iterateTautomers(mol, 'INCHI')
                        tautomers_list = [t.canonicalSmiles() for t in tautomers]
                        if len(tautomers_list) >= 0:
                            print(f"ID: {id}, Original SMILES: {smile}, Tautomers: {', '.join(tautomers_list)}")
                    except indigo.indigo.indigo_exception.IndigoException as e:
                        print(f"Failed to enumerate tautomers for ID: {id}, SMILES: {smile}")
                        continue
