import urllib
import xml.etree.ElementTree as ET

address=raw_input('Enter location:')

url=urllib.urlopen(address)
data=url.read()
# print data
tree=ET.fromstring(data)
counts=tree.findall('.//count')

sum=0
for item in counts:
    # print 'count:',item.text
    count=int(item.text)
    sum=sum+count

print sum
