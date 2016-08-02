import json
import urllib

url=raw_input('Enter url:')

uh=urllib.urlopen(url)
data=uh.read()

info=json.loads(data)
# print info["comments"]

sum=0
for item in info["comments"]:
    # print 'Count:',item["count"]
    sum=sum+item["count"]

print sum
