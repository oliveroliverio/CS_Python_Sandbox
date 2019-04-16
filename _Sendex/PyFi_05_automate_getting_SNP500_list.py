import bs4 as bs
import pickle
import requests

# go to a wikipedia page that updates the S&P500 list daily
# look at the source and find the 'table' tag.
# parse this w/ bs
def saveSP500Tickers():
    resp = requests.get('https://en.wikipedia.org/wiki/List_of_S%26P_500_companies')
    # specify parse in 2nd param below
    soup = bs.BeautifulSoup(resp.text, 'lxml')
    # specify the class of table between { } since you can have multiple tables
    table = soup.find('table', {'class':'wikitable sortable'})
    # init and empty tickers list
    tickers = []
    # 'tr' is 'table row.'  these are headers or titles of the columns
    for row in table.findAll('tr')[1:]:
        # 'td' is 'table data' at the zeroth column (or the left-most column  in the table, which is the ticker symbol)
        ticker = row.findAll('td')[0].text
        tickers.append(ticker)

    # save the list as pickle file, wb = write bytes
    with open("sp500tickers.pickle", "wb") as f:
        # dump tickers to file 'f'
        pickle.dump(tickers, f)

    print(tickers)
    return tickers

saveSP500Tickers()