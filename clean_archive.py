#!/usr/bin/env python
# coding: utf-8

import pandas as pd
import os
import glob
path = os.path.join("csv", "archiv")
destpath = os.path.join("csv","archive")
files = glob.glob(os.path.join(path,'*.csv'))
df = pd.DataFrame()

for file in files:
    df = pd.read_csv(file)
    cols = df.columns
    filename = file.split('/')[-1]
    print(filename)
    if "deaths" not in cols:
        print(cols)
        df['deaths'] = df.confirmed.str.extract(r'\((\d+)\)')
        df['confirmed']=df.confirmed.str.replace(r'(\d+) \(\d+\)',r'\1')
    df = df[['Bundesland','date', 'confirmed', 'deaths']]
    df.to_csv(os.path.join(destpath, filename), index=False)




