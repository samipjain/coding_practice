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

def search(root, val):
    if root is None:
        return False
    
    if (val > root.val):
        # right
        return search(root.right, val)
    elif (val < root.val):
        # left
        return search(root.left, val)
    else:
        # This is the value
        if (val == root.val):
            return True

if __name__ == "__main__":
    root = Node(5)
    root.left = Node(3)
    root.right = Node(6)
    root.left.left = Node(2)
    root.left.right = Node(4)
    root.right.right = Node(7)
    
    print(search(root,70))