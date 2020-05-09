class Node:
    def __init__(self, key):
        self.val = key
        self.left = None
        self.right = None

def printInorder(root):
    curr_node = root
    result = []
    stack = []
    while(curr_node != None or stack):
        while(curr_node != None):
            stack.append(curr_node)
            curr_node = curr_node.left
        curr_node = stack.pop()
        result.append(curr_node.val)
        curr_node = curr_node.right
    return result

if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)

    print(printInorder(root))