class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class singlelinkedlist:
    def __init__(self):
        self.head=None

    def delete_begining(self):
        temp=self.head
        self.head=temp.next
        temp.next=None

        
    def delete_position(self,pos):
        temp=self.head.next
        prev=self.head
        #2 iteraiton
        for i in range(1,pos-1):
            temp=temp.next
            prev=prev.next
        prev.next=temp.next
        temp.next=None


    def delete_last(self):
        temp=self.head.next
        prev=self.head
        while temp.next is not None:
            temp=temp.next
            prev=prev.next                
        prev.next = None 


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





obj=singlelinkedlist()
n=Node(10)
obj.head=n
n1=Node(20)
n.next=n1
n2=Node(30)
n1.next=n2
n3=Node(40)
n2.next=n3
n4=Node(50)
n3.next=n4
obj.display()

print("\ndelete at pos 3")
obj.delete_position(3)
obj.display()
print("\nDelete Last")
obj.delete_last()
obj.display()
print("\nDelete Beg")
obj.delete_begining()
obj.display()
