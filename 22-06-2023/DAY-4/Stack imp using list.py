stack=[]
def push():
    e=int(input("Enter the Element"))
    stack.append(e)
    print(stack)

def pop_element():
    if not stack:
        print("Stack is Empty")
    else:
        e=stack.pop()
        print("Removed element:",e)
        print(stack)

def display():
    if not stack:
        print("Stack is Empty")
    else:
        print(stack)
        
def peek():
    print("The top element is ",stack[len(stack)-1])
    
while True:
    print("Select Operation 1.Push 2.Pop 3.Peek 4.Display 5.Quit")
    c=int(input())
    if c==1:
        push()
    elif c==2:
        pop_element()
    elif c==5:
        break
    elif c==4:
        display()
    elif c==3:
        peek()
    else:
        print("Enter thr Coorect Operation")
