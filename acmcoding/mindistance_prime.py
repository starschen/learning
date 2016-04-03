#encoding:utf8
##p 这个是自己写的，但是是有问题的，先放下，重新写
import numpy as np

#输入
# vertex=raw_input().split(' ')    #定义图的顶点，输入格式0 1 2 3 4 5……顶点相当于矩阵下标或是矩阵索引
# graph_weight=[]               #定义图的邻接矩阵   图的邻接矩阵未相邻的点及对角线的值均为0
# for i in range(0,len(vertex)):
#     graph_weight.append(raw_input().split(' '))    #输入格式矩阵一行之间用空格分格，换列回车  取得邻接矩阵
# graph_weight=np.array(graph_weight,dtype=int)    #输入时解释为str，此处将其更改为int

#定义prime算法
def prime(graph_weight):
    vertex=map(str,range(0,len(graph_weight)))   #定义图的顶点,顶点为string
    print 'vertex:' vertex
    vertex_tree=vertex[0]        #定义最小生成树顶点集合,从0开始矩阵下标
    print 'vertex_tree:' vertex_tree
    min_spanning_tree=[]        #定义最小生成树邻接矩阵，prime算法是从任意点出发，此算法定义从0点出发
    while not(vertex_tree==vertex):          #最小生成树遍历所有顶点后结束循环
        for i in range(0,len(vertex_tree)):
            for j in range(0,len(vertex)):
                #if graph_weight[i][j]>0:
                min_weight=min(graph_weight[i])  #min(graph_weight[i]) 取与第i个顶点相邻的所有顶点中的最小值
                graph_weight_index=graph_weight.index(min_weight)  #graph_weight.index()取第i个点与其相邻结点中最小值的索引
                vertex_tree.append(graph_weight_index)    #vertex_tree.append()将其最小值的邻接点加入最小生成树的顶点中
                min_spanning_tree[j][graph_weight_index]=min_weight #将权值加入到最小生成树的矩阵里
            min_weight=0  #在原邻接矩阵中将取出的最小值置为0

    return min_spanning_tree

l1=[0,6,1,5,0,0]
l2=[0,0,5,0,0,0]
l3=[0,0,0,5,6,4]
l4=[0,0,0,0,5,2]
l5=[0,0,0,0,0,6]
l6=[0,0,0,0,0,0]

l=[l1,l2,l3,l4,l5,l6]
print prime(l)
