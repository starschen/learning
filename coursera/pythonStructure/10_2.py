name = raw_input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)

counts=dict()
times=[]
for line in handle:
    line=line.rstrip()
    if not line.startswith('From'):
        continue
    else:
        line=line.split()
        if len(line)<6:
            continue
        else:
            times.append(line[5])

for time in times:
    time=time.split(':')[0]
    # print time
    counts[time]=counts.get(time,0)+1

for k in sorted(counts):
    print k,counts[k]
