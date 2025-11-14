import os 
import pandas as pd 
# Base directory 
Base = r'C:/Users/hammad/Desktop/MSC IT Part1/Data Science'

# Input file (make sure the file exists here)
sFileName = os.path.join(Base, 'IP_DATA_ALL.csv')
print('Loading:', sFileName)

# Read CSV 
IP_DATA_ALL = pd.read_csv(sFileName, header=0, low_memory=False, encoding="latin-1")

# Output directory
sFileDir = os.path.join(Base, 'Output')
if not os.path.exists(sFileDir): 
    os.makedirs(sFileDir) 
 
# Show rows and columns
print('Rows:', IP_DATA_ALL.shape[0])
print('Columns:', IP_DATA_ALL.shape[1])
print('### Raw Data Set Columns #############')
for col in IP_DATA_ALL.columns: 
    print(col, type(col)) 
 
IP_DATA_ALL_FIX = IP_DATA_ALL.copy()
for i in range(len(IP_DATA_ALL_FIX.columns)):
    cNameOld = IP_DATA_ALL_FIX.columns[i]
    cNameNew = cNameOld.strip().replace(" ", ".") 
    IP_DATA_ALL_FIX.columns.values[i] = cNameNew 
 
# Set row IDs 
IP_DATA_ALL_FIX.index.names = ['RowID'] 
 
print('### Fixed Data Set Columns #################')
for col in IP_DATA_ALL_FIX.columns: 
    print(col, type(col)) 
 
sFileName2 = os.path.join(sFileDir, 'Retrieve_IP_DATA.csv') 
IP_DATA_ALL_FIX.to_csv(sFileName2, index=True, encoding="latin-1") 
 
print('### Done!! #############') 
 
