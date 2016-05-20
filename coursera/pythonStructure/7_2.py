# Use the file name mbox-short.txt as the file name
fname = raw_input("Enter file name: ")
fh = open(fname)
tot=0.0
count=0
for line in fh:
    line=line.rstrip()
    if not line.startswith("X-DSPAM-Confidence:") : continue
    tot+=float(line.split(':')[1])
    count+=1
print 'Average spam confidence:',tot/count
