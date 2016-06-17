name = raw_input("Enter file:")
if len(name) < 1 :
    name = "mbox-short.txt"
handle = open(name)
counts=dict()
mailNames=[]
for line in handle:
    line=line.rstrip()
    if not line.startswith('From '):
        continue
    else:
        mailNames.append(line.split()[1])
# print mailName

for name in mailNames:
    counts[name]=counts.get(name,0)+1
# print counts

bigcount=None
bigname=None
for name,count in counts.items():
    if bigcount==None or count>bigcount:
        bigcount=count
        bigname=name

print bigname,bigcount
