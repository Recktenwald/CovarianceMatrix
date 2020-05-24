# -*- coding: utf-8 -*-
"""
Created on Tue May 19 12:04:38 2020

@author: rener
"""
import numpy as np
import pandas as pd
import os
from datetime import date
import time
dir_path = os.path.dirname(os.path.realpath(__file__))
os.chdir(dir_path)

# %%
API_KEY = 'demo' # YOUR API KEY GOES HERE
ts = 'TIME_SERIES_WEEKLY'
# Example API Call
# https://www.alphavantage.co/query?
# function=TIME_SERIES_WEEKLY
# &symbol=IBM
# &apikey=demo&
# datatype=csv
#
# Call Alphavantage


def avApi_build(function: str, symbol: str, apikey: str,
                datatype: str = 'csv') -> str:
    return('https://www.alphavantage.co/query?'
           + 'function=' + function
           + '&symbol=' + symbol
           + '&apikey=' + apikey
           + '&datatype=' + datatype)


# %%
# Safe all timeseries in .csv with the name of the company and the current date
tickers = pd.read_csv('EuroStoxx50.csv')
today = date.today().strftime('%Y-%m-%d')
# %%
#   Later we want to concat all the dataframes, so it will be convenient to have
#   columns which just contain the ticker symbol and the name.

for i in range(len(tickers)):
    df=pd.read_csv(avApi_build(
            ts,
            tickers['Ticker'][i],
            API_KEY),
        index_col=0)
    df['symbol']=tickers['Ticker'][i]
    df['name']=tickers['Name'][i]
    df.to_csv('Stocks/' +
            tickers['Name'][i] +
            today +
        '.csv')
    time.sleep(15)

