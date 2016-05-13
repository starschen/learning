def selSort(l):
    pre=0
    while pre!=len(l):
        for i in range(pre,len(l)):
            if l[pre]>l[i]:
                l[pre],l[i]=l[i],l[pre]
        pre+=1
    print l

l=[9,5,7,4,6,1,3]
print selSort(l)
