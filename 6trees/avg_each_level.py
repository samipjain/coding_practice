class Tree:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
    
    def printLevelOrder(self, root):
        result = []
        queue = [root]
        avg = 0

        while queue:
            count = len(queue)
            avgstack = []
            while count > 0:
                node = queue.pop(0)
                avgstack.append(node.val)
                print(node.val, end=' ')
                if node.left is not None:
                    queue.append(node.left)
                if node.right is not None:
                    queue.append(node.right)
                count -= 1
            print(' ')
            avg = sum(avgstack)/len(avgstack)
            result.append(avg)
        return result
    

if __name__ == "__main__":
    root = Tree(3)
    root.left = Tree(9)
    root.right = Tree(20)
    root.right.left = Tree(15)
    root.right.right = Tree(7)

    print(root.printLevelOrder(root))
