import sys
import os
from datetime import datetime
from pytz import timezone
import pandas as pd
from sqlalchemy import create_engine
import uuid

# Ignore minor warnings
pd.options.mode.chained_assignment = None

# ------------------------------------------
# 1  Base folder setup
# ------------------------------------------
Base = r' '
print('################################')
print('Working Base:', Base, 'using', sys.platform)
print('################################')

# File & company names (just for reference)
Company = '01-Vermeulen'
InputFileName = 'VehicleData.csv'

# ------------------------------------------
# 2  MySQL Database connection
# ------------------------------------------
db_user = 'root'
db_pass = 'root'        # <-- change this if your MySQL password is different
db_host = 'localhost'
db_name = 'ClarkDB'

# Create database connection using SQLAlchemy
engine = create_engine(f'mysql+pymysql://{db_user}:{db_pass}@{db_host}/{db_name}')

# ------------------------------------------
# 3  Time details (example data)
# ------------------------------------------
print('\n#################################')
print('Time Category')

# UTC time
BirthDateUTC = datetime(1960, 12, 20, 10, 15, 0)
BirthDateZoneUTC = BirthDateUTC.replace(tzinfo=timezone('UTC'))
print('UTC Time:', BirthDateZoneUTC.strftime("%Y-%m-%d %H:%M:%S (%Z) (%z)"))

# Convert UTC time to Reykjavik timezone
BirthZone = 'Atlantic/Reykjavik'
BirthDateLocal = BirthDateZoneUTC.astimezone(timezone(BirthZone))
print('Reykjavik Time:', BirthDateLocal.strftime("%Y-%m-%d %H:%M:%S (%Z) (%z)"))

# ------------------------------------------
# 4 Create a DataFrame for Time data
# ------------------------------------------
IDZoneNumber = str(uuid.uuid4())   # Unique ID
sDateTimeKey = BirthDateZoneUTC.strftime("%Y-%m-%d-%H-%M-%S")

TimeFrame = pd.DataFrame({
    'IDNumber': [IDZoneNumber],
    'ZoneBaseKey': ['UTC'],
    'DateTimeKey': [sDateTimeKey],
    'UTCDateTimeValue': [BirthDateZoneUTC],
    'Zone': [BirthZone],
    'DateTimeValue': [BirthDateLocal.strftime("%Y-%m-%d %H:%M:%S")]
})

# ------------------------------------------
# 5  Store Time data in MySQL
# ------------------------------------------
TimeHub = TimeFrame[['IDNumber', 'ZoneBaseKey', 'DateTimeKey', 'DateTimeValue']]
print('\nSaving table: hub_time_gunnarsson')
TimeHub.to_sql('hub_time_gunnarsson', engine, if_exists="replace", index=False)

print('Saving table: dim_time_gunnarsson')
TimeHub.to_sql('dim_time_gunnarsson', engine, if_exists="replace", index=False)

# ------------------------------------------
# 6 Satellite-Time table
# ------------------------------------------
TimeSatellite = TimeFrame[['IDNumber', 'DateTimeKey', 'Zone', 'DateTimeValue']]
BirthZoneFix = BirthZone.replace('/', '_').lower()

sat_table = f'satellite_time_{BirthZoneFix}_gunnarsson'
dim_sat_table = f'dim_time_{BirthZoneFix}_gunnarsson'

print('\nSaving table:', sat_table)
TimeSatellite.to_sql(sat_table, engine, if_exists="replace", index=False)

print('Saving table:', dim_sat_table)
TimeSatellite.to_sql(dim_sat_table, engine, if_exists="replace", index=False)

# ------------------------------------------
# 7 Person Information
# ------------------------------------------
print("\n#################################")
FirstName = 'Gudmundur'
LastName = 'Gunnarsson'

IDPersonNumber = str(uuid.uuid4())

PersonFrame = pd.DataFrame({
    'IDNumber': [IDPersonNumber],
    'FirstName': [FirstName],
    'LastName': [LastName],
    'Zone': ['UTC'],
    'DateTimeValue': [BirthDateZoneUTC.strftime("%Y-%m-%d %H:%M:%S")]
})

print('\nSaving table: hub_person_gunnarsson')
PersonFrame.to_sql('hub_person_gunnarsson', engine, if_exists="replace", index=False)

print('Saving table: dim_person_gunnarsson')
PersonFrame.to_sql('dim_person_gunnarsson', engine, if_exists="replace", index=False)

# ------------------------------------------
#  Final message
# ------------------------------------------
print("\nAll transformation steps completed successfully!")
print("#############################################")

