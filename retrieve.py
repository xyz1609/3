import pandas as pd

# Load file
df = pd.read_csv(r"C:/Users/hammad/Desktop/MSC IT Part1/Data Science/IP_DATA_ALL.csv")

print("DATA INFO:")
print(df.info())
print(df.head())

# Fix names
df = df.rename(columns={
    "Place Name": "Place_Name",
    "Post Code": "Post_Code",
    "First IP Number": "First_IP_Number",
    "Last IP Number": "Last_IP_Number"
})

print("\nDATATYPES:")
print(df.dtypes)

print("\nCOUNTRY FREQUENCY:")
print(df["Country"].value_counts())

print("\nLATITUDE FREQUENCY:")
print(df["Latitude"].value_counts())

# Latitude stats
lat = df["Latitude"]
print("\nLATITUDE STATS:")
print("Min     :", lat.min())
print("Max     :", lat.max())
print("Mean    :", lat.mean())
print("Median  :", lat.median())
print("Range   :", (lat.min(), lat.max()))
print("Quantiles:\n", lat.quantile([0, .25, .5, .75, 1]))
print("Std Dev :", lat.std())

# Longitude
print("\nLONGITUDE STATS:")
print("Std Dev :", df["Longitude"].std())
