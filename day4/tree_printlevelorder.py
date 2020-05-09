class Node:
    def __init__(self, key):
        self.val = key
        self.left = None
        self.right = None

def printLevelOrder(root):
    if root is None:
        return
    
    queue = []
    result = []
    queue.append(root)
    
    while(queue):
        temp_result = []
        rowSize= len(queue)

        while(rowSize > 0):
            node = queue.pop(0)
            if node.left is not None:
                queue.append(node.left)
            if node.right is not None:
                queue.append(node.right)
            temp_result.append(node.val)
            rowSize -= 1
        result.append(temp_result)
    print(result)

if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)

    printLevelOrder(root)