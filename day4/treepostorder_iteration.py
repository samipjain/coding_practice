class Node:
    def __init__(self, key):
        self.val = key
        self.left = None
        self.right = None

def printPostorder(root):
    if root is None:
        return []
    else:
        result = []
        stack = []
        stack.append(root)
        while(stack):
            curr_node = stack.pop()
            result.append(curr_node.val)
            if (curr_node.left):
                stack.append(curr_node.left)
            if (curr_node.right):
                stack.append(curr_node.right)
             
        return result[::-1]

if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)

    print(printPostorder(root))