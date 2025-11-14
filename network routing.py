import os
import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt

Base = r"C:\Users\hammad\Desktop\MSC IT Part1\Data Science"
Company = r"01-Vermeulen"

f1 = os.path.join(Base, "Retrieve_Country_Code.csv")
f2 = os.path.join(Base,  "Retrieve_Router_Location.csv")
f3 = os.path.join(Base, "Retrieve_IP_DATA.csv")

out_dir = os.path.join(Base, Company, "02-Assess/01-EDS/02-Python")
os.makedirs(out_dir, exist_ok=True)

print("Loading files...")

Country = pd.read_csv(f1, encoding="latin1")[["Country", "ISO-2-CODE"]]
Country.rename(columns={"Country": "Country_Name",
                        "ISO-2-CODE": "Country_Code"}, inplace=True)

CompanyData = pd.read_csv(f2, encoding="latin1")
CompanyData.rename(columns={"Country": "Country_Code"}, inplace=True)

Customer = pd.read_csv(f3, encoding="latin1", low_memory=False).dropna()
Customer.rename(columns={"Country": "Country_Code"}, inplace=True)

print("Customer Columns:", Customer.columns.tolist())

print("Merging data...")
Merged = pd.merge(CompanyData, Country, on="Country_Code", how="inner")

out_file = os.path.join(out_dir, "Assess-Network-Routing-Company.csv")
Merged.to_csv(out_file, index=False, encoding="latin1")
print("Stored:", out_file)

# ---------------------------------------------------------
#   NETWORK GRAPH (USE First.IP.Number as IP Source)
# ---------------------------------------------------------

IP_COL = "First.IP.Number"

print("Building Network Graph...")

G = nx.from_pandas_edgelist(Customer, source=IP_COL, target="Country_Code")

plt.figure(figsize=(12, 7))
nx.draw_networkx(G, with_labels=True, node_size=700, font_size=7)
plt.title("Network Routing Diagram", fontsize=14)
plt.tight_layout()
plt.show()

print("Done!")
