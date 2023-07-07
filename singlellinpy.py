class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class SLL:
    def __init__(self):
        self.head=None
    
    def insert_beginning(self,data):
        nb=Node(data)
        nb.next=self.head
        self.head=nb
       
        
    def insert_end(self,data):
        ne=Node(data)
        temp=self.head
        while temp.next:
            temp=temp.next
        temp.next=ne
        ne.next=None
    
    def insert_position(self,pos,data):
        np=Node(data)
        temp=self.head
        for i in range(pos-1):
            temp=temp.next
        np.next=temp.next
        temp.next=np
        
    def delete_firstnode(self):
        temp=self.head
        self.head=temp.next
        temp.next=None
        
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
         
    #searching for an ele in ll
    def search(self,num):
        temp=self.head
        while temp:
            if temp.data==num:
                print("found")
                break
            temp=temp.next
    
    def display(self):
        if self.head is None:
            print("Linked list is empty")
        else:
            temp=self.head #temp=first node
            while temp:
                if temp.next is not None:
                    print(temp.data,"->",end=' ')
                else:
                    print(temp.data,end=' ') #temp.data means first node's data
                temp=temp.next#establishing link
                
obj=SLL()
#node creation_initialising
n=Node(10)#so n.data in Node class will be 10
obj.head=n   #assigning first node as head
n1=Node(20)
n.next=n1 #next node value
n2=Node(30)
n1.next=n2
n3=Node(40)
n2.next=n3
n4=Node(50)
n3.next=n4
n5=Node(60)
n4.next=n5
print("before inserting 100")
obj.display()
print(" ")
print("after inserting 100 at begin")
obj.insert_beginning(100)
obj.display() #traverse
print(" ")
print("after inserting 555 at bagin")
obj.insert_beginning(555)
obj.display()
print(" ")
print("after inserting 100 at end")
obj.insert_end(100)
obj.display()
print(" ")
print("after inserting at pos")
obj.insert_position(9,1000)
obj.display()
print(" ")
print("after deleting the first node")
obj.delete_firstnode()
obj.display()
print(" ")
print("after deleting the last node")
obj.delete_lastnode()
obj.display()
print(" ")
print("after deleting the position of a node")
obj.delete_pos(3)
obj.display()
print(" ")
num=int(input("enter the number"))
obj.search(num)