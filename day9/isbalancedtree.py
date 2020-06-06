class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value

def height(root):
    if root is None:
        return 0

    lheight = height(root.left)
    rheight = height(root.right)

    return max(lheight, rheight) + 1

def isBalanced(root):
    if root is None:
        return True
    
    lheight = height(root.left)
    rheight = height(root.right)

    if (abs(lheight - rheight) > 1):
        return False
    
    return isBalanced(root.left) and isBalanced(root.right)

if __name__ == "__main__":
    root = Node('a')
    root.left = Node('b')
    root.right = Node('c')
    root.left.left = Node('d')
    root.left.left.left = Node('e')
    root.right.right = Node('f')
    root.right.right.rightt = Node('g')
    

    print(isBalanced(root))
    