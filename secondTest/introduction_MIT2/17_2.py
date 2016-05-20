#encoding:utf8
class Node(object):
    def __init__(self,name):
        self.name=name
    def getName(self):
        return self.name
    def __str__(self):
        return self.name

class Edge(object):
    def __init__(self,src,dest):
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
        self.src=src
        self.dest=dest
        self.weight=weight
    def getWeight(self):
        return self.weight
    def __str__(self):
        return self.src.getName()+'->('+str(self.weight)+')'+self.dest.getName()

class Digraph(object):
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
        if not (src in self.nodes and dest in self.nodes):
            raise ValueError('Node not in graph')
        self.edges[src].append(dest)
    def childreOf(self,node):
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

def printPath(path):
    result=''
    for i in range(len(path)):
        result=result+str(path[i])
        if i!=len(path)-1:
            result=result+'->'
    return result

def DFS(graph,start,end,path,shortest):
    path=path+[start]
    print 'Current DFS path:',printPath(path)
    if start==end:
        return path
    for node in graph.childreOf(start):
        if node not in path:
            if shortest==None or len(path)<len(shortest):
                newPath=DFS(graph,node,end,path,shortest)
                if newPath!=None:
                    shortest=newPath
    return shortest

def BFS(graph,start,end):
    initPath=[start]
    pathQueue=[initPath]
    while len(pathQueue)!=0:
        tmpPath=pathQueue.pop(0)
        print 'Current BFS path:',printPath(tmpPath)
        lastNode=tmpPath[-1]
        if lastNode==end:
            return tmpPath
        for nextNode in graph.childreOf(lastNode):
            if nextNode not in tmpPath:
                newPath=tmpPath+[nextNode]
                pathQueue.append(newPath)
    return None


def search(graph,start,end):
    return DFS(graph,start,end,[],None)

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
    # sp=search(g,nodes[0],nodes[5])
    sp=BFS(g,nodes[0],nodes[5])
    # print 'Shortest path found by DFS:',printPath(sp)
    print 'Shortest path found by BFS:',printPath(sp)
testSP()
