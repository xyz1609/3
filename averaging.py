import pandas as pd   # Import pandas library for data handling

# Input and output file names
InputFileName = 'IP_DATA_CORE.csv'
OutputFileName = 'Retrieve_Router_Location.csv'

# Set the base directory path
Base = 'C:/Users/hammad/Desktop/MSC IT Part1/Data Science'
print('Working Base :', Base, 'using')

# Create full file path for input file
sFileName = Base + '/' + InputFileName
print('Loading :', sFileName)

# Read specific columns from the CSV file
IP_DATA_ALL = pd.read_csv(sFileName, header=0, low_memory=False,
                          usecols=['Country', 'Place Name', 'Latitude', 'Longitude'], encoding="latin-1")

# Rename column to remove space in the name
IP_DATA_ALL.rename(columns={'Place Name': 'Place_Name'}, inplace=True)

# Select required columns for further processing
AllData = IP_DATA_ALL[['Country', 'Place_Name', 'Latitude']]
print('All Data')
print(AllData)

# Group data by Country and Place_Name, then find the mean of Latitude
MeanData = AllData.groupby(['Country', 'Place_Name'])['Latitude'].mean()

# Display the grouped mean latitude data
print('Mean Data')
print(MeanData)
