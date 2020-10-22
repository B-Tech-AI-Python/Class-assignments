import pandas as pd
import numpy as np

print()

s1 = pd.Series([3, np.nan, 5, np.nan])
print(s1)

print()
d1 = pd.date_range('20010412', periods=4)
print(d1)

print()
df1 = pd.DataFrame({'A': d1,
                    'B': s1,
                    'C': pd.Series(1,index=list(range(4))),
                    'D': ['Who', 'What', 'Why', 'When']})

print(df1)

print()
print(df1.head())

print()
print(df1.tail())

print()
print(df1.shape)

print()
print(df1.index)

print()
print(df1.describe())

print()
print(df1.columns)

print()
print(df1.values)

print()
print(df1.sort_index(axis=1))

print()
print(df1.sort_values('D'))

print()
print(df1.ndim)


print()
