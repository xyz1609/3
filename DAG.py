# DAG.py (SHORT + GRAPH DISPLAY)
import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
import os, sys

Base = r"C:\Users\hammad\Desktop\MSC IT Part1\Data Science"
Company = r"01-Vermeulen"

print("### Working Base:", Base, "using", sys.platform)

file = os.path.join(Base, "Retrieve_Router_Location.csv")
out_dir = os.path.join(Base, Company, "02-Assess", "01-EDS", "02-Python")
os.makedirs(out_dir, exist_ok=True)

# ----- LOAD -----
df = pd.read_csv(file, encoding="latin1")
print(df.head(), "\nRows:", len(df))

countries = df["Country"].tolist()
places = (df["Place_Name"] + "-" + df["Country"]).tolist()

# ----- BUILD DAGs -----
G1 = nx.DiGraph([(countries[i], countries[i+1]) for i in range(len(countries)-1)])
G2 = nx.DiGraph([(places[i], places[i+1]) for i in range(len(places)-1)])

# ----- DRAW FUNCTION -----
def save_graph(G, path, size=(12,7)):
    plt.figure(figsize=size)
    nx.draw(G, with_labels=True, node_size=3000)
    plt.savefig(path)
    plt.show()

# ----- SAVE & SHOW -----
save_graph(G1, os.path.join(out_dir, "Assess-DAG-Company-Country.png"))
save_graph(G2, os.path.join(out_dir, "Assess-DAG-Company-Country-Place.png"))

print("### Done!")
