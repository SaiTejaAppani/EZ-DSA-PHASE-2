queue=[]
def enqueue():
    e=input("Enter element")
    queue.append(e)
    print(e,"is added in Q")

def dequeue():
    if not queue:
        print("Q is empty")
    else:
        e=queue.pop(0)
        print("Removed Element",e)

def display():
    print(queue)

while True:
    print("Select operation 1.Add 2.Remove 3.Show")
    c=int(input())
    if c==1:
        enqueue()
    elif c==2:
        dequeue()
    elif c==3:
        display()
    elif c==4:
        break
    else:
        print("ENter correct option")
                                    
