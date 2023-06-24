#Creating node-- Declaration and definition
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class singlelinkedlist:
    def __init__(self):
        self.head=None

    def display(self):
        if self.head is None:
            print("linked list is empty")
        else:
            temp=self.head    #temp=first node
            while temp:
                if temp.next!=None:
                    print(temp.data,end=" -> ")
                    temp=temp.next
                else:
                    print(temp.data,end=" ")#temp.data means first node's data
                    temp=temp.next

    def search(self,num):
        temp=self.head
        while temp is not None:
            if temp.data==num:
                print("FOund")
                return
            temp=temp.next
        print("Not Foound")
                

obj=singlelinkedlist()
#Node creation - initializing
n=Node(10) #So n.data in Node class will be 10
obj.head=n

n1=Node(20)
n.next=n1 #Next Node value

n2=Node(30)
n1.next=n2

n3=Node(40)
n2.next=n3

n4=Node(50)
n3.next=n4

n5=Node(60)
n4.next=None

obj.display()
print()
obj.search(50)
obj.search(445)
