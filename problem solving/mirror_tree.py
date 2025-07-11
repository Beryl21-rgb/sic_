class Node:
    def __init__(self, info): 
        self.info = info  
        self.left = None  
        self.right = None 

    def __str__(self):
        return str(self.info) 
    
class BinarySearchTree:
    def __init__(self): 
        self.root = None

    def create(self, val):  
        if self.root is None:
            self.root = Node(val)
        else:
            current = self.root
            while True:
                if val < current.info:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(val)
                        break
                elif val > current.info:
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(val)
                        break
                else:
                    # value already exists, do nothing
                    break

def mirror_tree(root):
    if root is None:
        return None
    
    # Swap left and right children
    root.left, root.right = root.right, root.left
    
    # Recursively mirror left subtree
    mirror_tree(root.left)
    
    # Recursively mirror right subtree
    mirror_tree(root.right)
    
    return root

def print_inorder(root):
    if root is None:
        return
    print_inorder(root.left)
    print(root.info, end=' ')
    print_inorder(root.right)

# Build tree manually
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.left.right.right= Node(4)
root.left.right.right.right = Node(9) 

print("Original inorder traversal:")
print_inorder(root)
print()

# Mirror the tree
mirror_tree(root)

print("Inorder traversal after mirroring:")
print_inorder(root)
print()
