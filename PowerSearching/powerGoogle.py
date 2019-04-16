#!/usr/bin/env python
import requests, sys, webbrowser, bs4

searchTerm = 'python multiple monitors'

print('Googling...')
#res = requests.get('http://google.com/search?q=' + ' '.join(sys.argv[1:]))
res = requests.get('http://google.com/search?q=' + ' '+ searchTerm)
res.raise_for_status()
res.raise_for_status()

# retrieve top search results links
soup = bs4.BeautifulSoup(res.text)

# open browser tab for each result
linkElems = soup.select('.r a')
numOpen = min(10, len(linkElems))
for i in range(numOpen):
    webbrowser.open('http://google.com' + linkElems[i].get('href'))

# usage:  python powerGoogle.py <searchTerm>