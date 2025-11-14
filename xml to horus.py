import xml.etree.ElementTree as ET
import pandas as pd

# --- Convert XML to DataFrame ---
def xml_to_df(xml_data):
    root = ET.fromstring(xml_data)
    rows = [{child.tag: child.text for child in entry} for entry in root]
    return pd.DataFrame(rows)

# --- Read XML File ---
input_file = r'C:\Users\hammad\Desktop\MSC IT Part1\Data Science\Country_Code.xml'
with open(input_file, 'r', encoding='utf-8') as f:
    xml_data = f.read()

print('============= INPUT DATA =============')
print(xml_data)
print('======================================')

# --- Process Data ---
df = xml_to_df(xml_data)

# Drop unwanted columns
df.drop(columns=[c for c in ['ISO2', 'ISO3'] if c in df.columns], inplace=True)

# Rename columns
df.rename(columns={'Country': 'CountryName', 'ISO-M49': 'CountryNumber'}, inplace=True)

# Set index and sort
if 'CountryNumber' in df.columns:
    df.set_index('CountryNumber', inplace=True)
if 'CountryName' in df.columns:
    df.sort_values('CountryName', ascending=False, inplace=True)

print('============= PROCESSED DATA =============')
print(df)
print('==========================================')

# --- Save to CSV ---
output_file = r'C:\Users\hammad\Desktop\MSC IT Part1\Data Science\HORUSXML-Country.csv'
df.to_csv(output_file, index=False)

print('============= XML to HORUS - Done =============')
