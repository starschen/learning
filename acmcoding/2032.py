#encoding:utf8
#2032杨辉三角

#这道题基本上不会，所以参考了百度百科上的答案
def pas_triangles():
    a=[1]
    while True:
        yield a
        a=[sum(i) for i in zip([0]+a,a+[0])]

n=int(raw_input())
g=pas_triangles()
for i in range(n):
    print next(g)
