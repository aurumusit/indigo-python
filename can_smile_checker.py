import indigo

# Initialize a set to store the can_smiles from the main_dataset
main_can_smiles = set()

# Read the main_dataset and store the can_smiles
with open("csv/converted_smiles_using_indigo.csv", "r") as main_file:
    next(main_file)  # Skip the header line
    for line in main_file:
        parts = line.strip().split(",")
        if len(parts) >= 3:
            can_smile = parts[2]  # Assuming the can_smile is the third value
            main_can_smiles.add(can_smile)

# Initialize Indigo
indigo_instance = indigo.Indigo()
# Initialize a counter variable
match_count = 0

# Process the new_dataset
with open("csv/new_dataset.csv", "r") as new_file:
    next(new_file)  # Skip the header line
    for line in new_file:
        parts = line.strip().split(",")  
        if len(parts) == 2:
            id, smile = parts[0], parts[1]
        
            # Convert SMILES to canonical SMILES using Indigo
            mol = indigo_instance.loadMolecule(smile)
            can_smile = mol.canonicalSmiles()
        
            # Check if the canonical SMILES exists in the main_dataset can_smiles set
            if can_smile in main_can_smiles:
                print(f"ID: {id}, Canonical SMILES: {can_smile} - Already Exists in main_dataset")
                match_count += 1

            else:
                print(f"ID: {id}, Canonical SMILES: {can_smile} - Not Found in main_dataset")
        else:
            print(f"Line with incorrect format: {line.strip()}")

print(f"Total matched can_smiles: {match_count}")


# Get the Indigo version using an alternative method
indigo_version = indigo_instance.version()
print(f"Indigo version: {indigo_version}")

