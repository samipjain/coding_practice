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

def insertIntoBST(root, val):
    if root is None:
        root = Node(val)
        return root
    if val > root.val:
        # right
        if root.right is not None:
            insertIntoBST(root.right, val)
        else:
            root.right = Node(val)
    else:
        # left
        if root.left is not None:
            insertIntoBST(root.left, val)
        else:
            root.left = Node(val)
    return root

def 

if __name__ == "__main__":
    root = Node(4)
    root.left = Node(2)
    root.right = Node(7)
    root.left.left = Node(1)
    root.left.right = Node(3)
    
    printLevelOrder(insertIntoBST(root, 5))
    printLevelOrder(insertIntoBST(root, 8))
    printLevelOrder(insertIntoBST(root, 0))