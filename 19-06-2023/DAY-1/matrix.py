n=int(input("enter the size of the matrix"))
matrix=[]
for i in range(0,n):
    r=[]
    for j in range(0,n):
        r.append(int(input()))
    matrix.append(r)
    
#printing the matrix
for i in range(0,n):
    for j in range(0,n):
        print(matrix[i][j],end=" ")
    print("")
#
DE=[]
NDE=[]
UDE=[]
LDE=[]
for i in range(0,n):
    for j in range(0,n):
        if i==j:
            DE.append(matrix[i][j])
        if i!=j:
            NDE.append(matrix[i][j])
        if i<j:
            UDE.append(matrix[i][j])
        if i>j:
            LDE.append(matrix[i][j])
print("Diagonal elements:",DE)
print("Non-Diagonal elements:",NDE)
print("Upper-Diagonal elements:",UDE)
print("Lower-Diagonal elements:",LDE)

 
for i in range(0,n):
    for j in range(0,n):
        if i==j:
            print(matrix[i][j],end=" ")
        else:
            print(" ",end=" ")
    print("")

for i in range(0,n):
    for j in range(0,n):
        if i!=j:
            print(matrix[i][j],end=" ")
        else:
            print(" ",end=" ")
    print("")
