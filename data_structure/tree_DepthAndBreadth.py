#encoding:utf8
#二叉树的深度优先遍历／广度优先遍历

#代码来源：http://www.jianshu.com/p/7d665f3c01bc
class Node:
    def __init__(self,data,left,right):
        self.data=data
        self.left=left
        self.right=right

class BinaryTree:
    def __init__(self):
        self.root=None

    def make_tree(self,node):
        self.root=node

    def insert(self,node):
        lst=[]
        def insert_node(tree_node,p,node):
            if tree_node.left==None:
                tree_node.left=node
                lst.append(tree_node.left)
                return
            elif tree_node.right==None:
                tree_node.right=node
                lst.append(tree_node.right)
                return
            else:
                lst.append(tree_node.left)
                lst.append(tree_node.right)
                if p>(len(lst)-2):    #????
                    return
                else:
                    insert_node(lst[p+1],p+1,node)

        lst.append(self.root)
        insert_node(self.root,0,node)

def breadth_tree(tree):
    lst=[]

    def traverse(node,p):
        if node.left!=None:
            lst.append(node.left)
        if node.right!=None:
            lst.append(node.right)
        if p>(len(lst)-2):
            return
        else:
            traverse(lst[p+1],p+1)

    lst.append(tree.root)
    traverse(tree.root,0)

    for node in lst:
        print node.data

def depth_tree(tree):
    lst=[]
    lst.append(tree.root)
    while len(lst)>0:
        node=lst.pop()
        print node.data
        if node.right!=None:
            lst.append(node.right)
        if node.left!=None:
            lst.append(node.left)


if __name__=='__main__':
    lst=[12,9,7,19,3,8,52,106,70,29,20,16,8,50,22,19]
    tree=BinaryTree()
    for (i,j) in enumerate(lst):
        node=Node(j,None,None)
        if i==0:
            tree.make_tree(node)
        else:
            tree.insert(node)

    breadth_tree(tree)
    print '\n'
    depth_tree(tree)
