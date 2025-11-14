import pandas as pd
from cryptography.fernet import Fernet

# Data
df = pd.DataFrame({
    'Name': ['Sejal', 'Sanskruti', 'Srushiti'],
    'Age': [28, 24, 30],
    'Salary': [50000, 60000, 55000],
    'Gender': ['Female', 'Female', 'Female']
})

# Horizontal
def horizontal(df):
    print("\nHorizontal Style:")
    print(df)

# Vertical
def vertical(df):
    print("\nVertical Style:")
    print(pd.melt(df, id_vars='Name', var_name='Attribute', value_name='Value'))

# Island
def island(df):
    print("\nIsland Style:")
    for name, group in df.groupby('Name'):
        print(f"\nIsland for {name}:")
        print(group)

# Secure Vault (Encrypt + Decrypt)
def secure_vault(df, col):
    print("\nSecure Vault Style (Encrypted Salary):")
    key = Fernet.generate_key()
    cipher = Fernet(key)

    df2 = df.copy()
    df2['Encrypted_' + col] = df[col].apply(lambda x: cipher.encrypt(str(x).encode()).decode())
    df2 = df2.drop(columns=[col])
    print(df2)

    print("\nDecrypted Salary:")
    print(df2[['Name']].assign(
        **{'Decrypted_' + col: df2['Encrypted_' + col].apply(lambda x: cipher.decrypt(x.encode()).decode())}
    ))

# Run all
horizontal(df)
vertical(df)
island(df)
secure_vault(df, 'Salary')
