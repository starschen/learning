#encoding:utf8
#2020绝对值排序 

#思路：这道题原本想到用sorted将绝对值排序，再set去重，但是发现set在去重的过程中会将列表排序，
#我想这道题较笨的方法就是遍历列表元素的绝对值比较大小，同时将重复值去掉
#我又笨了，这明明是一道三行代码就可以搞定的，我又想复杂了，python真是高级啊，其实我真的不大会
#正经的写按大小排序，有现成的还是先用着吧

def seq_abs(l):
    lst=sorted(l[1:],key=lambda x:abs(x),reverse=1)
    print lst

seq_abs([3,3,-4,2])
seq_abs([4,0,1,2,-3])
