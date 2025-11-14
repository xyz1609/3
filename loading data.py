# Retrieve-IP_DATA_ALL.py
import os
import pandas as pd

# Base directory
Base = r' '

# Input file
input_file = os.path.join(Base, "IP_DATA_ALL.csv")
print("Loading :", input_file)

# Read CSV
df = pd.read_csv(input_file, header=0, low_memory=False, encoding="latin-1")

# Output folder
output_dir = os.path.join(Base, "Retrieve")
os.makedirs(output_dir, exist_ok=True)

# Basic info
print("Rows:", df.shape[0])
print("Columns:", df.shape[1])

print("Raw Data Set #####################################")
for col in df.columns:
    print(" ", col, type(col))

# Fix column names
df2 = df.copy()
df2.columns = [c.strip().replace(" ", ".") for c in df2.columns]

print("Fixed Data Set ###################################")
for col in df2.columns:
    print(" ", col, type(col))

print("Fixed Data Set with ID")
df2.index.name = "RowID"

# Save file
output_file = os.path.join(output_dir, "Retrieve_IP_DATA.csv")
df2.to_csv(output_file, index=True, encoding="latin-1")

print("## Done!! ########################################")

