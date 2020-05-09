class Node:
    def __init__(self, key):
        self.val = key
        self.left = None
        self.right = None

def printPreorder(root):
    result = []
    stack = []
    stack.append(root)
    while(stack):
        curr_node = stack.pop()
        result.append(curr_node.val)
        if (curr_node.right):
            stack.append(curr_node.right)
        if (curr_node.left):
            stack.append(curr_node.left) 
    return result

if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)

    print(printPreorder(root))