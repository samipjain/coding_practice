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

def hasPathSum(root, sum):
    if root is None:
        return False
    
    sum = sum - root.val
    if (sum == 0 and root.left is None and root.right is None):
        return True

    return hasPathSum(root.left, sum) or hasPathSum(root.right, sum)

if __name__ == "__main__":
    root = Node(5)
    root.left = Node(4)
    root.right = Node(8)
    root.left.left = Node(11)
    root.left.left.left = Node(7)
    root.left.left.left = Node(2)
    root.right.left = Node(13)
    root.right.right = Node(4)
    root.right.right.right = Node(1)   
    
    print(hasPathSum(root, 22))