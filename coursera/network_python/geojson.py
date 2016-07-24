import urllib
import json

serviceurl='http://maps.googleapis.com/maps/api/geocode/json?'

while True:
    address=raw_input('Enter location:')
    if len(address)<1:break

    url=serviceurl+urllib.urlencode({'sensor':'false','address':address})
    print 'Retrieving',url
    uh=urllib.urlopen(url)
    data=uh.read()
