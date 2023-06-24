#Get one dynamic array for the given size and do all the operations of ds(insert,delete,search,sort)?
def array():

    while(1):
        print("1.insert")
        print("2.delete")
        print("3.search")
        print("4.sort")
        print("5.display")
        option=int(input())
        if option==1:
            insert()
        elif option==2:
            delete()
        elif option==3:
            search()
        elif option==4:
            sorting()
        elif option==5:
            display()
        elif option==6:
            break
        else:
            print("entered wrong option")
def insert():
    n=int(input("enter:"))
    a.append(int(input()))
    print(a)
def delete():
    d=int(input("enter element to delete:"))
    a.remove(d)
    print("element is deleted")
def search():
    s=int(input("enter element:"))
    f=0
    for i in a:
        if i==s:
            f=1
    if f==1:
        print("element found")
    else:
        print("element not found")
def sorting():
    a.sort()
    print(a)
def display():
    print(a)

print("enter size:")
n=int(input())
print("enter:")
a=[]
for i in range(0,n):
    a.append(int(input()))
print(a)
array()
            
            
    
    

        
