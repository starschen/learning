#encoding:utf8
#二叉树的遍历

#代码来源：http://blog.csdn.net/littlethunder/article/details/9707669，仅学习用
class Node:
    def __init__(self,value=None,left=None,right=None):
        self.value=value
        self.left=left
        self.right=right

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
    if len(preList)==0:    #树为空时
        return
    elif len(preList)==1:   #树只有根结点
        afterList.append(preList[0])
        return
    root=preList[0]     #前序遍历的第一个元素为根结点
    n=midList.index(root)      #在中序遍历中找到根结点所在的位置，结点左为左子树，右为右子树
    #前序遍历中第1到n的元素左子树，同时1为左子树的根
    findTree(preList[1:n+1],midList[:n],afterList) #这部分不太能理解，midList不应该是左子树范围吗？
    findTree(preList[n+1:],midList[n+1:],afterList)
    afterList.append(root)
    return afterList

print findTree(preList,midList,afterList)
