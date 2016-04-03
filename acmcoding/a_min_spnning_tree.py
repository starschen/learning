#encoding:utf8
##1.清空生成树，任取一个顶点加入生成树
##2.在那些一个端点在生成树里，另一个端点不在生成树里的边中，选取一条权最小的边，将它和另一个端点加进生成树
##3.重复步骤2，直到所有的顶点都进入了生成树为止，此时的生成树就是最小生成树


def prime(graph):
    nodes=range(len(graph))

    v=[0]   #顶点集合
    e=[]    #边集合

    while len(v)!=len(graph):
        min_lengh=0
        for i in v:
            for j in range(1,len(graph)):
                if j not in v and graph[i][j]!=0:
                    if min_lengh==0 or graph[i][j]<min_lengh:
                        min_lengh=graph[i][j]
                        edge=(i,j)
        v.append(edge[1])
        e.append(edge)

    print v
    print e


l1=[0,6,1,5,0,0]
l2=[0,0,5,0,0,0]
l3=[0,0,0,5,6,4]
l4=[0,0,0,0,5,2]
l5=[0,0,0,0,0,6]
l6=[0,0,0,0,0,0]


l=[l1,l2,l3,l4,l5,l6]
prime(l)

##2
# import numpy as np
# def min_spanning_tree(g,n):   #n为结点数
#     dis=[0]*n     #距离初始化
#     pre=[0]*n
#     flag=[False]*n    #生成树结点初始化
#     flag[0]=True    #从第一个点开始
#     k=0
#
#     for i in range(n):
#         dis[i]=g[k][i]     #将与k连接的边权值加到dis里
#     for j in range(n-1):   #从剩下的n-1个结点中找最小的距离
#         min=dis[0]
#         for i in range(n):
#             if min>dis[i] and not flag[i]: #找最小边的点，且这个点没有加入到生成树中
#                 min=dis[i]
#                 k=i        #找到相邻的最小的边
#         if k==0:        #不连通
#             return
#         flag[k]=True    #将k加入到生成树结点中
#         for i in range(n):
#             if dis[i]>g[k][i] and not flag[i]:
#                 dis[i]=g[k][i]
#                 pre[i]=k
#
#     return dis,pre
#
# if __name__=='__main__':
#     n=6
#     l=[
#         [0,6,1,5,1000,1000],
#         [6,0,5,1000,1000,],
#         [1,5,0,5,6,4],
#         [5,1000,5,0,5,2],
#         [1000,6,5,0,6],
#         [1000,1000,4,2,6,0],
#     ]
#
#
# print min_spanning_tree(l,n)


##1
#输入
# nodes=raw_input().split(' ')    #定义图的顶点，输入格式0 1 2 3 4 5……顶点相当于矩阵下标或是矩阵索引
# edges_weight=[]               #定义图的邻接矩阵   图的邻接矩阵未相邻的点为空，对角线的值为0
# for i in range(0,len(nodes)):
#     edges_weight.append(raw_input().split(' '))    #输入格式矩阵一行之间用空格分格，换列回车  取得邻接矩阵
# edges_weight=np.array(edges_weight,dtype=int)    #输入时解释为str，此处将其更改为int

# def min_spanning_tree(g):
#     nodes=range(len(g))
#     nodes_tree=[nodes[0]]       #将第一个顶点放入生成树中
#     mst=[]
#     while nodes_tree!=nodes:
#         for j in nodes_tree:
#             for i in nodes:
#                 k=g.index(min(g[j]))   #取到权值最小边的点
#                 nodes_tree.append(k)         #将找到的最小权值对应的点加入到生成树结点中
#                 mst[j][i]=g[j][i]  #将这条边加入到最小生成树里
#
#         return mst
#
# l1=[0,6,1,5,0,0]
# l2=[0,0,5,0,0,0]
# l3=[0,0,0,5,6,4]
# l4=[0,0,0,0,5,2]
# l5=[0,0,0,0,0,6]
# l6=[0,0,0,0,0,0]
#
#
# l=[l1,l2,l3,l4,l5,l6]
# print min_spanning_tree(l)
