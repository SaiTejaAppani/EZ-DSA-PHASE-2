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

    def insert_atend(self,data):
        ne=Node(data)
        temp=self.head
        while temp.next:
            temp=temp.next
        temp.next=ne
        ne.next=None

        
    def display(self):
        if self.head is None:
            print("Linked list is empty")
        else:
            temp=self.head #temp=frist node
            while temp.next:
                print(temp.data,end="->")
                #temp.data means first node data
                temp=temp.next#establishing link
            print(temp.data)
obj=SLL()
#node creation-initializing
n=Node(10)#so n.data in Node calss will be 10
obj.head=n
n1=Node(20)
obj.head.next=n1
n2=Node(30)
n1.next=n2
n3=Node(40)
n2.next=n3
obj.display()

print("After insert begin")
obj.insert_beginning(100)
obj.display()
print("AT END")
obj.insert_atend(70)
obj.display()
