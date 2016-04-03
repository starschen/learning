#encoding:utf8
#海选女主角

def find_max(m,n,l):
    max_num=l[0][0]
    dic={}
    for i in range(0,m):
        for j in range(0,n):
            if abs(l[i][j])>abs(max_num):
                max_num=l[i][j]
                # dic={max_num:(i,j)}  ##这个与下两句都可以实现题目要求。
                if max_num not in dic: ##这两名虽然可以实现题要求，但是我打印出dic，两种出现的结果是不一样的，还是没太想通是怎么回事。
                    dic[max_num]=(i+1,j+1)

    # return dic
    return max_num,dic[max_num]




    #return dic.keys,dic.values



print find_max(2,3,[[1,4,-3],[-7,3,0]])
print find_max(3,4,[[1,3,-5,0],[2,-5,6,8],[5,-6,8,9]])
print find_max(3,4,[[1,3,-5,9],[2,-5,6,8],[5,-6,8,9]])
