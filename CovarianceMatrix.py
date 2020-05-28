# -*- coding: utf-8 -*-
"""
Created on Sat May 23 11:28:30 2020

@author: rener
"""

import numpy as np
import pandas as pd
import os
from datetime import date
import time
import sys
dir_path = os.path.dirname(os.path.realpath(__file__))
os.chdir(dir_path)

#%% For the various companies we have data going back differently far.
#   
#   

frames=[]
for file in os.listdir('Stocks'):
    frames.append(
        pd.read_csv('Stocks/' +file,index_col=0))
    
# For the various companies we have data going back differently far.
# So there is  decision to make: We could discard look for the shortest
# available timeseries, and trim all other datasets to the same length.
# But then whenever we compute a covariance for two longer datasets
# we will not use all available information.
# So we only trim every pair in the covariance computing function.


df=pd.concat(frames)

# Add column with Estimated Average of the day
df['EstAvg'] = df[['open','high','low','close']].apply(np.mean,axis=1)

df.to_csv('fulltable.csv')

#%%

pivot = df.pivot(columns = 'symbol', values = 'EstAvg')
# Note that we are taking the symbols from the Pivot Table.
# This is the case, because when the Alphavantage API does not give
# us a dataset for some symbol, it does not appear in the pivot table,
# so we avoid a Key Error.
symbols = pivot.columns

# Next we initialize an 'empty' dataframe, and start filling it.
CovMatrix = pd.DataFrame(index=symbols,columns=symbols)
#%%

def covariance(a,b):
    return np.mean((a-np.mean(a)*(b-np.mean(b))))

for col in CovMatrix:
    for row in CovMatrix.index:
        CovMatrix[row][col]=covariance(pivot[row], pivot[col])




