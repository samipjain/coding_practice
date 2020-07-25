class Tree:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
    
    # Faster
    def add(self, node, value):
        if node == None:
            node = Tree(value)
        elif value < node.val:
            return self.add(node.left, value)
        else:
            return self.add(node.right, value)
        

    def printLevelOrder(self, root):
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
    root = Tree(10)
    root.left = Tree(5)
    root.right = Tree(12)
    root.left.left = Tree(3)
    root.left.right = Tree(8)

    print(root.add(root, 18))
    print(root.printLevelOrder(root))