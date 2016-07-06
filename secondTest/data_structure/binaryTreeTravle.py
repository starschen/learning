#encoding:utf8
#二叉树的遍历(前、中、后)


class Node:
    def __init__(self,value=None,right=None,left=None):
        self.value=value
        self.right=right
        self.left=left

class BinaryTree(object):
    def __init__(self):
        self.root=Node()

    def add(self,value):
        node=Node(value)
        if self.isEmpty():
            self.root=node
        else:
            tree_node=self.root
            queue=[]
            queue.append(self.root)

            while queue:
                tree_node=queue.pop(0)
                if tree_node.left==None:
                    tree_node.left=node
                    return
                elif tree_node.right==None:
                    tree_node.right=node
                    return
                else:
                    queue.append(tree_node.left)
                    queue.append(tree_node.right)

def preTraverse(root):
    if root==None:
        return
    print root.value
    preTraverse(root.left)
    preTraverse(root.right)

def midTraverse(root):
    if root==None:
        return
    midTraverse(root.left)
    print root.value
    midTraverse(root.right)

def afterTraverse(root):
    if root==None:
        return
    afterTraverse(root.left)
    afterTraverse(root.right)
    print root.value

if __name__=='__main__':
    root=Node('D',Node('B',Node('A'),Node('C')),Node('E',right=Node('G',Node('F'))))
    print '前序遍历：'
    preTraverse(root)
    print '中序遍历：'
    midTraverse(root)
    print '后序遍历：'
    afterTraverse(root)
    print '\n'

#已知先序遍历结果和中序遍历求后序遍历
preList=list('DBACEGF')
midList=list('ABCDEFG')
afterList=[]

def findTree(preList,midList,afterList):
    if len(preList)==0:
        return
    elif len(preList)==1:
        afterList.append(preList[0])
        return
    root=preList[0]
    n=midList.index(root)
    findTree(preList[1:n+1],midList[:n],afterList)
    findTree(preList[n+1:],midList[n+1:],afterList)
    afterList.append(root)
    return afterList

print findTree(preList,midList,afterList)
