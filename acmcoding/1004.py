#encoding:utf8
#1004 let the balloon rise

n=int(raw_input())
l=[]
lst=[]
count=0
for i in range(n):
    l.append(raw_input())
print l
for i in range(n):
    for j in range(n):
        if l[i]==l[j] and i!=j:
            lst.append(l[i])
print lst
            #count+=1
