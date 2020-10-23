import pandas as pd
import numpy as np

df = pd.DataFrame({'Dates': pd.date_range('20010412', periods=4),
                    'NaN': pd.Series([3, np.nan, 5, np.nan]),
                    'One': pd.Series(1,index=list(range(4))),
                    'Www': ['Who', 'What', 'Why', 'When']})

print("\nData frame----------------")
print(df)

print("\ndf[:1]----------------")
print(df[:1])

print("\ndf.Dates----------------")
print(df.Dates)

print("\ndf.loc[0]----------------")
print(df.loc[0])

print("\ndf.loc[:,['Dates','Www']]----------------")
print(df.loc[:,['Dates','Www']])

print("\ndf.loc[1,'Dates']----------------")
print(df.loc[1,'Dates'])

print("\ndf.loc[:,'NaN'] > 0----------------")
print(df.loc[:,'NaN'] > 0)

print("\ndf.iloc[2]----------------")
print(df.iloc[2])

print("\ndf.iloc[3:5, 0:2]----------------")
print(df.iloc[3:5, 0:2])

print("\ndf['NaN'] >= 3----------------")
print(df['NaN'] >= 3)

print("\ndf['NaN'] >= 3----------------")
print(df['NaN'] >= 3)
