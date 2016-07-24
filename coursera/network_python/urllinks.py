# Note - this code must run in Python 2.x and you must download
# http://www.pythonlearn.com/code/BeautifulSoup.py
# Into the same folder as this program

import urllib
from BeautifulSoup import *

url = raw_input('Enter URL:')
count=int(raw_input('Enter count:'))
position=int(raw_input('Enter position:'))



def get_next_one(position, url):
    print 'Retrieving:', url
    html = urllib.urlopen(url).read()
    soup = BeautifulSoup(html)
    # Retrieve all of the anchor tags
    tag = soup('a')[position]
    next_url = tag.get('href', None)
    return next_url

for i in range(count+1):
    url = get_next_one(position-1, url)
