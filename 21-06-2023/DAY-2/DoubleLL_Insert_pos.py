class Node:
    def __init__(self,data):
        self.data=data
        self.pprev=None
        self.next=None
class dll:
    def __init__(self):
        self.head=None

    def display(self):
        if self.head is None:
            print("Empty")
        else:
            temp=self.head
            while temp:
                if temp.next is None:
                    print(temp.data,end=" ")
                else:
                    print(temp.data,"<-->",end=" ")
                temp=temp.next


    def insert_position(self,pos,data):
        n=Node(data)
        temp=self.head
        for i in range(1,pos-1):
            temp=temp.next

        n.next=temp.next
        temp.next=n
        

    
obj=dll()

n1=Node(100)
obj.head=n1

n2=Node(200)
n1.next=n2
n2.prev=n1

n3=Node(300)
n2.next=n3
n3.prev=n2

obj.display()
print()
print("INserting 150 at pos 2")
obj.insert_position(2,150)
obj.display()
