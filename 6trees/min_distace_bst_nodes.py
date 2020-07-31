class Tree:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    prev = float('-inf')
    result = float('inf')
    
    def minDiffInBST(self, root):
        if root is None:
            return
        
        self.minDiffInBST(root.left)
        
        self.result = min(self.result, abs(root.val - self.prev))
        self.prev = root.val

        self.minDiffInBST(root.right)
        return self.result

if __name__ == "__main__":
    # root = Tree(4)
    # root.left = Tree(2)
    # root.right = Tree(6)
    # root.left.left = Tree(1)
    # root.left.right = Tree(3)

    root = Tree(27)
    root.right = Tree(34)
    root.right.right = Tree(58)
    root.right.right.left = Tree(50)
    root.right.right.left.left = Tree(44)

    print(root.minDiffInBST(root))