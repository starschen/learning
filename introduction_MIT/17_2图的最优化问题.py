#encoding:utf8
#17_2图的最优化问题.py
#节点和边
class Node(object):
    def __init__(self,name):
        '''assume name is string'''
        self.name=name
    def getName(self):
        return self.name
    def __str__(self):
        return self.name

class Edge(object):
    def __init__(self,src,dest):
        '''assume src and dest are nodes'''
        self.src=src
        self.dest=dest
    def getSource(self):
        return self.src
    def getDestination(self):
        return self.dest
    def __str__(self):
        return self.src.getName()+'->'+self.dest.getName()

class WeightedEdge(Edge):
    def __init__(self,src,dest,weight=1.0):
        '''assume src and dest are nodes,weight is float'''
        self.src=src
        self.dest=dest
        self.weight=weight
    def getWeight(self):
        return self.weight
    def __str__(self):
        return self.src.getName()+'->('+str(self.weight)+')'+self.dest.getName()

#有向图和无向图
class Digraph(object):
    #节点是图中的一组点
    #边是将每个节点映射为它的一组子节点的字典映射
    def __init__(self):
        self.nodes=[]
        self.edges={}
    def addNode(self,node):
        if node in self.nodes:
            raise ValueError('Duplicate node')
        else:
            self.nodes.append(node)
            self.edges[node]=[]
    def addEdge(self,edge):
        src=edge.getSource()
        dest=edge.getDestination()
        if not(src in self.nodes and dest in self.nodes):
            raise ValueError('Node not in graph')
        self.edges[src].append(dest)
    def childrenOf(self,node):
        return self.edges[node]
    def hasNode(self,node):
        return node in self.nodes
    def __str__(self):
        result=''
        for src in self.nodes:
            for dest in self.edges[src]:
                result=result+src.getName()+'->'+dest.getName()+'\n'
        return result[:-1]

class Graph(Digraph):
    def addEdge(self,edge):
        Digraph.addEdge(self,edge)
        rev=Edge(edge.getDestination(),edge.getSource())
        Digraph.addEdge(self,rev)
#使用深度优先搜索算法寻找最短路径
def printPath(path):
    '''path is a list of nodes'''
    result=''
    for i in range(len(path)):
        result=result+str(path[i])
        if i!=len(path)-1:
            result=result+'->'
    return result

def DFS(graph,start,end,path,shortest):
    '''假定graph是无向图，首尾者是节点，Path是节点列表，返回无向图中从头到尾的最短路径'''
    path=path+[start]
    print 'Current DFS path:',printPath(path)
    if start==end:
        return path
    for node in graph.childrenOf(start):
        if node not in path: #avoid cycles
            if shortest==None or len(path)<len(shortest):
            #用来判断是否需要继续搜索这条路径，如果已经比当前最短路径要长，就不需要继续搜索
                newPath=DFS(graph,node,end,path,shortest)
                if newPath!=None:
                    shortest=newPath
    return shortest

def search(graph,start,end):
    '''假设这个图是无向图，首尾都是节点，返回无向图中从头到尾的最短路径'''
    return DFS(graph,start,end,[],None)#path=[]表示当前已经搜索过的路径为空，shortest=None表示还没有找到到的路径

#使用广度优先搜索算法寻找最短路径
def BFS(graph,start,end):
    '''假定graph是一个Digraph，假定start和end是graph中的节点'''
    initPath=[start]
    pathQueue=[initPath]
    while len(pathQueue)!=0:
        #获取并删除pathQueue中最早的节点
        tmpPath=pathQueue.pop(0)
        print 'Current BFS path:',printPath(tmpPath)
        lastNode=tmpPath[-1]
        if lastNode==end:
            return tmpPath
        for nextNode in graph.childrenOf(lastNode):
            if nextNode not in tmpPath:
                newPath=tmpPath+[nextNode]
                pathQueue.append(newPath)
    return None

#测试深度优先搜索代码
def testSP():
    nodes=[]
    for name in range(6):
        nodes.append(Node(str(name)))
    g=Digraph()
    for n in nodes:
        g.addNode(n)
    g.addEdge(Edge(nodes[0],nodes[1]))
    g.addEdge(Edge(nodes[1],nodes[2]))
    g.addEdge(Edge(nodes[2],nodes[3]))
    g.addEdge(Edge(nodes[2],nodes[4]))
    g.addEdge(Edge(nodes[3],nodes[4]))
    g.addEdge(Edge(nodes[3],nodes[5]))
    g.addEdge(Edge(nodes[0],nodes[2]))
    g.addEdge(Edge(nodes[1],nodes[0]))
    g.addEdge(Edge(nodes[3],nodes[1]))
    g.addEdge(Edge(nodes[4],nodes[0]))
    g.addEdge(Edge(nodes[0],nodes[5]))
    # sp=search(g,nodes[0],nodes[5]) #深度优先
    # print 'Shortest path found by DFS:',printPath(sp) #这部分打印出来的是有问题的
    sp=BFS(g,nodes[0],nodes[5]) #广度优先
    print 'Shortest path found by BFS:',printPath(sp)#这部分打印出来的是有问题的

testSP()
