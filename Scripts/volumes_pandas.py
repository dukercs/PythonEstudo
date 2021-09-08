import pandas as pd
import csv

jsonfile = '/home/dukercs/pasa/discos_us-east.json'

df = pd.read_json(jsonfile, )
df = pd.DataFrame(df)

# print(df)

# df = df.iloc(-1)


dftop = df.head()

#print(dftop)

df.to_csv(r'volumes_us-east.csv', header=True)


