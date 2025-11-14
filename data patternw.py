import pandas as pd
import re
# Load file
file_name = ' '
df = pd.read_csv(file_name, dtype=str, low_memory=False)

# Function to generate pattern
def make_pattern(s: str) -> str:
    if pd.isna(s):
        return ""
    s=str(s)

    # Replace letters with A s =
    s=re.sub(r"[A-Za-z]", "A", s)

    #Replace digits with N
    s=re.sub(r"[0-9]", "N", s)

    # Replace spaces with b
    s = s.replace("","b")

    # Replace all other characters with u
    s =re.sub(r"[^ANb]", "u", s)
    return s

# Apply to Country column df_patterns = pd.DataFrame({ "Country":
df_patterns=pd.DataFrame({"Country":df["Country"].unique()})
df_patterns["PatternCountry"]=df_patterns["Country"].apply(make_pattern)
print(df_patterns.head())

