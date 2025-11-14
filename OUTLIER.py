import pandas as pd

# Paths
Base = r"C:/Users/hammad/Desktop/MSC IT Part1/Data Science"
print("Working Base:", Base)

df = pd.read_csv(Base + "/IP_DATA_CORE.csv",
                 usecols=["Country", "Place Name", "Latitude", "Longitude"],
                 encoding="latin-1")

df = df.rename(columns={"Place Name": "Place_Name"})

# Filter only London
LON = df[df["Place_Name"] == "London"][["Country", "Place_Name", "Latitude"]]
print("\nAll Data:\n", LON)

# Mean & STD
mean = LON["Latitude"].mean()
std = LON["Latitude"].std()

upper = mean + std
lower = mean - std

print("\nOutliers (High > {:.3f}):".format(upper))
print(LON[LON["Latitude"] > upper])

print("\nOutliers (Low < {:.3f}):".format(lower))
print(LON[LON["Latitude"] < lower])

print("\nNot Outliers:")
print(LON[(LON["Latitude"] >= lower) & (LON["Latitude"] <= upper)])
