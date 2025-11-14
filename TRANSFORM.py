import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler, StandardScaler, OneHotEncoder

data = {
    'Age': [25, 32, 47, 51, 62],
    'Income': [50000, 60000, 120000, 100000, 110000],
    'Gender': ['Male', 'Female', 'Female', 'Male', 'Female'],
    'Purchased': ['No', 'Yes', 'No', 'Yes', 'Yes']
}

df = pd.DataFrame(data)
print("Original Data:")
print(df)

# Min-Max Scaling
scaler = MinMaxScaler()
df[['Age', 'Income']] = scaler.fit_transform(df[['Age', 'Income']])
print("\nNormalized Data (Min-Max Scaling):")
print(df)

# Standard Scaling
scaler = StandardScaler()
df[['Age', 'Income']] = scaler.fit_transform(df[['Age', 'Income']])
print("\nStandardized Data (Z-Score Scaling):")
print(df)

# Log Transformation
df['Log_Income'] = np.log(df['Income'] + 1)
print("\nData after Log Transformation of 'Income':")
print(df)

# One-Hot Encoding
encoder = OneHotEncoder(sparse_output=False)  # Change 'sparse' to 'sparse_output'
encoded_gender = encoder.fit_transform(df[['Gender']])
encoded_df = pd.DataFrame(encoded_gender, columns=encoder.get_feature_names_out(['Gender']))
df = pd.concat([df, encoded_df], axis=1).drop('Gender', axis=1)
print("\nData after One-Hot Encoding 'Gender':")
print(df)

# Binning Age
df['Age_Binned'] = pd.cut(df['Age'], bins=[0, 30, 50, 100], labels=['Young', 'Middle-aged', 'Senior'])
print("\nData after Binning 'Age':")
print(df)
