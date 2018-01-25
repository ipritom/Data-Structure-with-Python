#This Approch has reduced characters and LOC
class Node:
    def __init__(self,data):
        self.data = data
        self.next = next
class LL:
    def __init__(self,head=None,tail=None):
        self.head = head
        self.tail = head

    def insert(self,data):
        new_node = Node(data)
        new_node.next = None

        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
    def delete(self,value):
        cur = self.head
        pre = None
        f = False  #found or Not
        while cur!=None:
            if cur.data == value:
                if pre==None:
                    self.head = cur.next
                    f = True
                    break
                else:
                    pre.next = cur.next
                    f = True
                    break
            pre = cur
            cur = cur.next
        if f==True:
            print("Deleted")
        else:
            print("NOT FOUND")
    def reverese(self):
        cur = self.head
        pre = None
        while cur!=None:
            nNode = cur.next
            cur.next = pre
            pre = cur
            cur = nNode
        self.head = pre

        
    def display(self):
        cur = self.head
        while cur!=None:
            print(cur.data)
            cur = cur.next

ll = LL()
ll.insert(44)
ll.insert(55)
ll.insert(54)
ll.display()
