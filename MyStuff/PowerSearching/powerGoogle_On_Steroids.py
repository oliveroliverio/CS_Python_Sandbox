#!/usr/bin/env python
import requests, sys, webbrowser, bs4, os

# Example Search list below
# Before learning how to code VST plugins you should check out:
# - SynthEdit
# - SynthMaker
# - Reaktor
# - Max/MSP
# - PureData
# - CSound
# - SuperCollider
# - Bidule
# - Usine
# goal: open each of these terms in new window with 'n' tabs
#   for each search result.

# open file into variable
textFile = open('text files/ListOfSearchTerms2')

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
    os.system('open -na \'Google Chrome\'')
    # open browser tab for each result
    linkElems = soup.select('.r a')
    numOpen = min(3, len(linkElems))
    for i in range(numOpen):
        # this below doesn't work
        # webbrowser.open('http://google.com' + linkElems[i].get('href'))
        # needed to modify the above to below to get it to open new windows
        webbrowser.get(chrome_path).open('http://google.com' + linkElems[i].get('href'))

    #usage:  python powerGoogle.py <searchTerm>