# fname = raw_input("Enter file name: ")
fname='romeo.txt'
fh = open(fname)
lst = list()
for line in fh:
    l=line.rstrip().split()
    for i in l:
        if i not in lst:
            lst.append(i)
print sorted(lst)
