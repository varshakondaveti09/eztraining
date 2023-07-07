#creating a node in double ll
class Node:
    def __init__(self,data):
        self.data=data
        self.previous=None
        self.next=None
class DLL:
    def __init__(self):
        self.head=None
        
    def display(self):
        if self.head is None:
            print("Linked list is empty")
        else:
            temp=self.head #temp=first node
            while temp:
                if temp.next is not None:
                    print(temp.data,"<-->",end=' ')
                else:
                    print(temp.data,end=' ') #temp.data means first node's data
                temp=temp.next
    def insert_beginning(self,data):
        nb=Node(data)
        nb.next=self.head
        nb.prev=None
        self.head=nb
    
    def insert_end(self,data):
        ne=Node(data)
        temp=self.head
        while temp.next!=None:
            temp=temp.next
        temp.next=ne
        ne.prev=temp
        ne.next=None
        
    def insert_position(self,position,data):
        np=Node(data)
        temp=self.head
        for i in range(0,position-1):
            temp=temp.next
        np.next=temp.next
        temp.prev=np
        temp.next=np
        np.prev=np
        
    def delete_firstnode(self):
        temp=self.head
        self.head=temp.next
        temp.next=None
        self.head.prev=None
        
    def delete_lastnode(self):
        temp=self.head.next
        prev=self.head
        while temp.next is not None:
            temp=temp.next
            prev=prev.next
        prev.next=None
     
    def delete_pos(self,pos):
         temp=self.head.next
         prev=self.head
         for i in range(1,pos-1):
             temp=temp.next
             prev=prev.next
         prev.next=temp.next
         temp.next=None
         temp.prev=prev
        
obj=DLL()
#node creation_initialising
n=Node(10)#so n.data in Node class will be 10
obj.head=n   #assigning first node as head
n1=Node(20)
n.next=n1#next node value
n.previous=None
n2=Node(30)
n1.next=n2
n1.previous=n
n3=Node(40)
n2.next=n3
n2.previous=n1
n4=Node(50)
n3.next=n4
n3.previous=n2
n5=Node(60)
n4.next=n5
n4.previous=n3
obj.display()
print(" ")
print("inserting a node at begin")
obj.insert_beginning(100)
obj.display()
print(" ")
print("inserting a node at end")
obj.insert_end(70)
obj.display()
print(" ")
print("insertinga node at position")
obj.insert_position(4,80)
obj.display()
print(" ")
print("deleting a first node")
obj.delete_firstnode()
obj.display()
print(" ")
print("deleting a lastnode")
obj.delete_lastnode()
obj.display()
print(" ")
print("deleting a node at position")
obj.delete_pos(3)
obj.display()