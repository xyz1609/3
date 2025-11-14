import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt

# --- FILES ---
inp  = r"\Retrieve_Country_Code.csv"
out1 = r"\population.gml"
out2 = r"pulation.png"

# --- LOAD DATA ---
df = pd.read_csv(inp, encoding="latin1")
countries = df["Country"]
print(df.head(), "\nRows:", len(df))

# --- GRAPH ---
G = nx.path_graph(countries.tolist())   # same chain logic in one line
nx.write_gml(G, out1)

# --- DRAW ---
plt.figure(figsize=(18,18))
pos = nx.spring_layout(G, seed=42, k=0.25)

nx.draw(G, pos,
        node_size=50,
        width=0.3,
        with_labels=True,
        font_size=6,
        font_family="Arial")

plt.tight_layout()
plt.savefig(out2, dpi=300)
plt.show()

print("Done!")
