import pandas as pd
from pandas import ExcelFile
from pandas import ExcelWriter

path = "Z:\\Projects\\1-LOCA\\"

df = pd.read_excel(path+"HU4_plantWideData"+str(1)+".xlsm", sheet_name='DataQuery', skiprows=8, usecols="A:AN")

print (df.keys())