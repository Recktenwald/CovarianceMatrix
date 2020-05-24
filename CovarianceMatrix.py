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

#%% playground

df1=pd.read_csv('Stocks/Adidas2020-05-23.csv',index_col=0)
df2=pd.read_csv('Stocks/Ahold Delhaize2020-05-23.csv',index_col=0)

#%% For the various companies we have data going back differently far.
#   So we will want to trim everything down to the shortest time horizon we have
#   In order to have all data available at each time.
#   
#   

frames=[]
for file in os.listdir('Stocks'):
    frames.append(
        pd.read_csv('Stocks/' +file,index_col=0))
    
df=pd.concat(frames)
#%%
# Add column with Estimated Average of the day
df['EstAvg'] = df[['open','high','low','close']].apply(np.mean,axis=1)

#catch = df[df['symbol']=='ADS.DE']




