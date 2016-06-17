# fname = raw_input("Enter file name: ")
fname='mbox-short.txt'
if len(fname) < 1 : fname = "mbox-short.txt"
else:
    fh = open(fname)
    count = 0
    for line in fh:
        line=line.rstrip()
        if not line.startswith('From '):
            continue
        else:
            count+=1
            print line.split()[1]
print "There were", count, "lines in the file with From as the first word"
