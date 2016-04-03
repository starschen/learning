#encoding:utf8
##2041超级楼梯

##这道题原来思路不对，自己并没有想通该如何表示
##网上参考：每次有2种走法，并且要求最后还能干好到达M级。
##正着不行，逆向思维一下，要达到最后一级的前一级只能是M-1或者M-2；
##也就是说就是到达M-1的走法加上M-2的走法相加就等于到达最后一级的走法。
##所以递推公式：
##F(n)=F(n-1)+F(n-2);
##F（1）=1，F（2 ）=2；
##这就是斐波那契数列：每个数都等于它的前两个数字和（前2个除外）；

n=int(raw_input())
l=[]
for i in range(n):
    a=raw_input()
    l.append(a)
l=map(int,l)
#print l

def stages(m):
    if m==1 or m==2:
        return 1
    else:
        return stages(m-1)+stages(m-2)


for i in l:
    print stages(i)
