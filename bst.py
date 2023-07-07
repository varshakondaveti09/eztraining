class BST:
    def __init__(self,key):
        self.key = key
        self.l_child=None
        self.r_child=None
    def insert_node(self,data):
        if self.key is None:
            print("empty")
            return
        if self.key == data:
            print("data elements is already present")
            return
        if self.key > data:
            if self.l_child:
                self.l_child.insert_node(data)
            else:
                self.l_child=BST(data)
        else:
            if  self.r_child:
                self.r_child.insert_node(data)
            else:
                self.r_child=BST(data)
    def pre_order(self):
        print(self.key,end=" ")
        if self.l_child:
            self.l_child.pre_order()
        if self.r_child:
            self.r_child.pre_order()
root=BST(45)
root.insert_node(30)
print(root)
root.insert_node(50)
lst=[1,2,4,5,7,4,8,3,4,5]
root1=BST(5)
for i in lst:
    root1.insert_node(i)
root1.pre_order()