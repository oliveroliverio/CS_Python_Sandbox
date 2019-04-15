import bs4 as bs
import pickle
import requests
import datetime as dt
import pandas as pd
import pandas_datareader.data as web
import os


def saveSP500Tickers():
    resp = requests.get('https://en.wikipedia.org/wiki/List_of_S%26P_500_companies')
    soup = bs.BeautifulSoup(resp.text, 'lxml')
    table = soup.find('table', {'class':'wikitable sortable'})
    tickers = []
    for row in table.findAll('tr')[1:]:
        ticker = row.findAll('td')[0].text
        tickers.append(ticker)

    with open("sp500tickers.pickle", "wb") as f:
        # dump tickers to file 'f'
        pickle.dump(tickers, f)

    print(tickers)
    return tickers

def getDataFromYahoo(reload_sp500=False):
    if reload_sp500:  # if someone loads sp500 from before, get it from web
        tickers = saveSP500Tickers()
    else: # otherwise open from file, and rb or read bytes
        with open("sp500tickers.pickle", "rb") as f:
            tickers = pickle.load(f)

# want to store all data locally into CSV files since it takes awhile to reping them.
    if not os.path.exists('stock_dfs'):
        os.mkdirs('stock_dfs')

    start = dt.datetime(2018,1,1,)
    end = dt.datetime.now()

    for ticker in tickers:
        if not os.path.('stock_dfs/{}.csv'.format(ticker)):
            df = web.DataReader(ticker, 'yahoo', start, end)


