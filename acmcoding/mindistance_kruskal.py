#encoding:utf8
##输入：n个点的坐标
##输出：找到m个点，使得其它点距离m个点中的距离其最近的一点距离小于某值，输出这m个点，并输出其距离关系
#输入l=[(x1,y1),(,),()]
import math
from heapq import heappop, heappush
from itertools import count

from operator import itemgetter

class DisjointSet(dict):
    def add(self, item):
        self[item] = item

    def find(self, item):
        parent = self[item]

        while self[parent] != parent:
            parent = self[parent]

        self[item] = parent
        return parent

    def union(self, item1, item2):
        self[item2] = self[item1]

def kruskal( nodes, edges ):
    forest = DisjointSet()
    mst = []
    for n in nodes:
        forest.add( n )

    sz = len(nodes) - 1

    for e in sorted( edges, key=itemgetter( 2 ) ):
        n1, n2, _ = e
        t1 = forest.find(n1)
        t2 = forest.find(n2)
        if t1 != t2:
            mst.append(e)
            sz -= 1
            if sz == 0:
                return mst

            forest.union(t1, t2)
