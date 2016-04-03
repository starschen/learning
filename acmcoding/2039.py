#encoding:utf8
#2039三角形

def is_triangle(a,b,c):
    if a+b>c and a+c>b and b+c>a:
        print 'YES'
    else:
        print 'NO'


m=int(raw_input())
s=[]
for i in range(m):
    l=raw_input().split(' ')
    s.append(l)
print s

for i in range(m):
    is_triangle(s[i][0],s[i][1],s[i][2])
