class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.val = data

def insert(root, key):
    if root is None:
        return Node(key)
    elif key < root.val:
        root.left = insert(root.left, key)
    elif key > root.val:
        root.right = insert(root.right, key)
    return root

def inorder(root):
    if root:
        inorder(root.left)
        print(root.val, end=" ")
        inorder(root.right)

# Example usage:
# Create an empty binary search tree
bst = None

# Insert nodes into the binary search tree
bst = insert(bst, 50)
bst = insert(bst, 30)
bst = insert(bst, 20)
bst = insert(bst, 40)
bst = insert(bst, 70)
bst = insert(bst, 60)
bst = insert(bst, 80)

# Print the tree using inorder traversal
print("Inorder traversal:")
inorder(bst)
print()
