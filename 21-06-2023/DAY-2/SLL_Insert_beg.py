#creating node-declaration & defination
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        
class sll:
    def __init__(self):
        self.head=None

    def insert_beginning(self,data):
        nb=Node(data)
        nb.next=self.head
        self.head=nb

    def display(self):
        if self.head is None:
            print("linked list is empty")
        else:
            temp=self.head                  #temp=first node
            while temp:
                print(temp.data,"->",end=" ")
                                            #temp.data means first node's data
                temp=temp.next              #establishing link
obj=sll()
                    #node creation -initialising
n=Node(10)          #so n.data in node class will be 10
obj.head=n          #assigning first node as head node
n1=Node(20)
n.next=n1    #next node value
n2=Node(30)
n1.next=n2
print("Before inserting 100")
obj.display()
print("")
print("After insering 100")

obj.insert_beginning(100)
obj.display()
print("")
    
