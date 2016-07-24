# import urllib
# import urllib2
#
# data={}
# data['name']='WHY'
# data['location']='SDU'
# data['language']='Python'
#
# url_values=urllib.urlencode(data)
# print url_values
#
# #name=Somebody+Here&language=Python&location=Northampton  #???
# url='http://www.example.com/example.cgi'
# full_url=url+'?'+url_values
#
# req = urllib2.Request(full_url)
# rsp=urllib2.urlopen(req)
# print rsp.read()

import requests

url='http://www.example.com/example.cgi'
data={}
data['name']='WHY'
data['location']='SDU'
data['language']='Python'
r = requests.get(url, data=data)
print r.text
