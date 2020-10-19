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

