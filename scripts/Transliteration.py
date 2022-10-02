"""
Malayalam to Hindi transliteration
"""

import pandas as pd
# Load data

with open("/your_path/test.ml_XX", encoding='utf-8') as f:
    data_ml = f.read().splitlines()

data_hi = []

tab = pd.read_csv("Ml_Hi_LookupTable.csv", header=None, index_col=0)

for l in data_ml:
    txt = ""
    for i in l:
        try:
            txt += tab.loc[i,1]
        except KeyError:
            txt += i

    data_hi.append(txt)

with open("/your_path/test.trans.ml_XX", mode="w", encoding= 'utf-8') as f2:
    f2.write('\n'.join(data_hi))
