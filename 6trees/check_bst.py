class Tree:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
    
    def checkBST(self, root):
        return self.checkBSTUtil(root, float('-inf'), float('inf'))

    def checkBSTUtil(self, root, min, max):
        if root is None:
            return True
        
        if root.val < min or root.val > max:
            return False
        
        return self.checkBSTUtil(root.left, min, root.val) and self.checkBSTUtil(root.right, root.val, max)

if __name__ == "__main__":
    root = Tree(10)
    root.left = Tree(5)
    root.right = Tree(12)
    root.left.left = Tree(3)
    root.left.right = Tree(8)

    print(root.checkBST(root))