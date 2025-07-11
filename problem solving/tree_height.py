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

def height(root):
    if root is None:
        return -1   # empty tree has height -1
    left_depth = height(root.left)
    right_depth = height(root.right)
    return max(left_depth, right_depth) + 1

# Input and driver code
tree = BinarySearchTree()
t = int(input("Enter the number of elements: "))
arr = list(map(int, input("Enter elements: ").split()))

for i in range(t):
    tree.create(arr[i])

print(height(tree.root))
