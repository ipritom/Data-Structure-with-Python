#Linked List Ops: Insert Search Delete
class Node:
    def __init__(self,data=None,next_node=None):
        self.data = data
        self.next_node = next_node

    def get_data(self):
        return self.data
    def get_next(self):
        return self.next_node
    def set_next(self,new_next):
        self.next_node = new_next

class LinkedList:
    def __init__(self,head=None,tail=None):
        self.head = head
        self.tail = tail
    def insert(self,data):
        new_node = Node(data)
        new_node.set_next(None)
        if self.head==None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.set_next(new_node)
            self.tail = new_node
    def search(self,data):
        cur = self.head
        found = False
        while cur!=None:
            if cur.get_data()==data:
               found = True
            cur = cur.get_next()
        print(found)
    def delete(self,data):
        cur = self.head
        pre = None
        found = False
        #Two Conditions
        #1> While data in head 2>While data not in head
        while cur!=None: 
            if cur.get_data()==data: 
                if found==False:
                    self.head = cur.get_next()
                    found=True
                    break
                else:
                    pre.set_next(cur.get_next())
                    found = True
                    break
            pre = cur
            cur = cur.get_next()
        
        if found == True:
            print("DELETED")
        else:
            print("ELEMENT NOT FOUND")
        
            
    def display(self):
        cur = self.head
        while cur!=None:
            print(cur.get_data())
            cur = cur.get_next()

LL = LinkedList()
LL.insert(44)
LL.insert(55)
LL.insert(9)
LL.insert(5)
LL.display()
