#!/usr/bin/env python
import requests, sys, webbrowser, bs4, os

## Example Search list below
# trading Bull flag
# trading bear flag (bearish)
# trading flat top breakout
# trading 1234 pattern
# trading micro 1 minute pullback (bearish)
# trading red to green move
# trading open range breakout
# Goal: open each of these search terms in a new tab

# open file into variable
textFile = open('text files/ListOfSearchTerms_small')

# put words in text file into list called 'searchList'
searchList = textFile.read().split('\n')

chrome_path = 'open -a /Applications/Google\ Chrome.app %s'

for i in searchList:

    print('Googling...')
    #res = requests.get('http://google.com/search?q=' + ' '.join(sys.argv[1:]))
    res = requests.get('http://google.com/search?q=' + ' '+ i)
    res.raise_for_status()

    # retrieve top search results links
    soup = bs4.BeautifulSoup(res.text)

    # open a new chrome window
    # -n for new, -a for app
    # os.system('open -na \'Google Chrome\'')
    os.system('open -a \'Google Chrome\'')

    # open browser tab for each result
    linkElems = soup.select('.r a')
    numOpen = min(1, len(linkElems))
    for i in range(numOpen):
        # use below to keep in the same window
        # webbrowser.open('http://google.com' + linkElems[i].get('href'))
        # use below to open in new windows per search term
        webbrowser.get(chrome_path).open('http://google.com' + linkElems[i].get('href'))

    #usage:  python powerGoogle.py <searchTerm>


## ----------------Creating a class for distributing amongst multiple monitors

class Distribute2Monitors:

    def init