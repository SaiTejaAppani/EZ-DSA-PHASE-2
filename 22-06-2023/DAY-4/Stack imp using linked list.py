class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class stack:
    def __init__(self):
        self.head=None

    def push(self,data):
        if self.head is None:
            self.head= Node(data)
        else:
            new_node=Node(data)
            new_node.next=self.head
            self.head=new_node

    def pop(self):
        if self.head is None:
            return None
        else:
            popped=self.head.data
            self.head=self.head.next
            return popped

obj_stack=satck()
while true:
    print("push <value>")
    print("pop")
    print("Quit")
    do = input("What would you like to do")
    .split()
    print("do",do)
    print("do[0]",do[0])
    operation=do[0]
