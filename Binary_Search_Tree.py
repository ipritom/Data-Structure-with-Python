#BINARY Search Tree with preOrder Traversal

class Node:
    def __init__(self, data,left = None,right = None):
        self.data = data
        self.left = left
        self.right = right

class BST:
    def __init__(self,root=None):
        self.root = root
    def insert(self,val):
        new_node = Node(val)
        
        if self.root == None:
            self.root = new_node
                        
        else:           
            cur = self.root
            leaf = None
            while cur!=None:
                leaf = cur
                if val >= cur.data:
                    cur = cur.right
                else:
                    cur = cur.left
            if val >= leaf.data:
                leaf.right = new_node
            else:
                leaf.left = new_node

def preOrder(r):
    
    if r:
        print(r.data,end=' ')

        preOrder(r.left)
        preOrder(r.right)
            
        

b = BST()
b.insert(1)
b.insert(2)
b.insert(5)
b.insert(3)
b.insert(6)
b.insert(4)
preOrder(b.root)
'''
x = BST()
x.insert(3)
x.insert(2)
x.insert(1)
x.preOrder()'''


