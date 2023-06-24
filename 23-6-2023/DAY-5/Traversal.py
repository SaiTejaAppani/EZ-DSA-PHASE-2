class Node:
    def __init__(self,key):
        self.left= None
        self.right = None
        self.val = key


def printPreorder(root):
    if root:
         print(root.val,end=" -> ") #Then print the data of node
         printPreorder(root.left)#First recur on left child
         printPreorder(root.right)#Now recur on right child

def printInorder(root):
    if root:
        printInorder(root.left)#First recur on left child
        print(root.val,end=" -> ") #Then print the data of node
        printInorder(root.right)#Now recur on right child

def printPostorder(root):
    if root:
        printPostorder(root.left)#First recur on left child
        printPostorder(root.right)#Now recur on right child
        print(root.val,end=" -> ") #Then print the data of node

root=Node(1)
root.left=Node(2)
root.right=Node(3)
root.left.left=Node(4)
root.left.right=Node(5)
print("Pre-Order: ")
printPreorder(root)
print()
print("In-Order:  ")
printInorder(root)
print()
print("Post-Order:")
printPostorder(root)
