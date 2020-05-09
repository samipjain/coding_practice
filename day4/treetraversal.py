class Node:
    def __init__(self, key):
        self.val = key
        self.left = None
        self.right = None
    

def printPreorder(root):
    if (root):
        print(root.val),
        printPreorder(root.left)
        printPreorder(root.right)

def printInorder(root):
    if (root):
        printInorder(root.left)
        print(root.val),
        printInorder(root.right)

def printPostorder(root):
    if (root):
        printPostorder(root.left)
        printPostorder(root.right)
        print(root.val),

if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)

    printPreorder(root)
    printPostorder(root)
    printInorder(root)