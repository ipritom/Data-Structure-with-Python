#Linked List Implementation with Head and Tail
class Node:
    def __init__(self,data=None,next_node = None):
        self.data = data
        self.next_node = next_node

    def get_data(self):
        return self.data
    def get_next(self):
        return self.next_node
    def set_next(self,new_next):
        self.next_node = new_next
class LL:
    def __init__(self,head=None,tail=None):
        self.head = head   #head
        self.tail = tail   #tail
    def insert(self,data):
        new_node =  Node(data) #new_node
        #new_node.set_next(None)
        
        if self.head == None:
            #new_node.set_next(None)
            self.head = new_node
            self.tail = new_node
            
        else:
            self.tail.set_next(new_node) #tail --> floating node
            self.tail = new_node         #tail updated
            self.tail.set_next(self.head)#tail --> head (circle completed)
        
    def display(self):
        cur = self.head
        print(cur.get_data())
        cur = cur.get_next()
        while cur!=self.head:
            print(cur.get_data())
            cur = cur.get_next()

ll = LL()
ll.insert(5)
ll.insert(6)
ll.insert(8)
ll.insert(5)
ll.insert(6)
ll.insert(8)
ll.display()
