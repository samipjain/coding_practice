class Tree:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
    
    def getMin(self, root):
        if root.left is None:
            return root.val
        return self.getMin(root.left)

    def getMax(self, root):
        if root.right is None:
            return root.val
        return self.getMax(root.right)

         
if __name__ == "__main__":
    root = Tree(10)
    root.left = Tree(5)
    root.right = Tree(12)
    root.left.left = Tree(3)
    root.left.right = Tree(8)
    root.left.right.right = Tree(18)
    

    print(root.getMin(root))
    print(root.getMax(root))