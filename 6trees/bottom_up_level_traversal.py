class Tree:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
    
    def printLevelOrder(self, root):
        result = []
        queue = [root]

        while queue:
            count = len(queue)
            resstack = []
            while count > 0:
                node = queue.pop(0)
                resstack.append(node.val)
                print(node.val, end=' ')
                if node.left is not None:
                    queue.append(node.left)
                if node.right is not None:
                    queue.append(node.right)
                count -= 1
            print(' ')
            result.append(resstack)
        result.reverse()
        return result
    

if __name__ == "__main__":
    root = Tree(10)
    root.left = Tree(5)
    root.right = Tree(15)
    root.left.left = Tree(3)
    root.left.right = Tree(7)
    root.right.right = Tree(18)

    print(root.printLevelOrder(root))
