import housing_hidden
from sqlalchemy import create_engine
import pandas as pd

print("START")

db = housing_hidden.alchemy(housing_hidden.secrets())
crime_table = 'crime'
engine = create_engine(db)

crime_records = r'/Users/koonleong/Documents/UM MADS/SIADS 591/Project/data/michigan_offense_type_by_agency_2019.xlsx'
print('READING EXCEL')
crime_township = pd.read_excel(crime_records)
crime_township.fillna(0, inplace=True)
crime_township['Population'] = crime_township['Population'].astype("int32")
crime_township['TotalOffenses'] = crime_township['TotalOffenses'].astype("int32")

print('WRITING TO DATABASE')
crime_township.to_sql(crime_table, engine, if_exists = 'replace', index = True)

print("END")