class Tree:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        
        return abs(self.height(root.left)-self.height(root.right)) <= 1 and self.isBalanced(root.left) and self.isBalanced(root.right)
        
    def height(self, root):
        if root is None:
            return 0
        
        lheight = self.height(root.left)
        rheight = self.height(root.right)
        
        return 1+max(lheight, rheight)

if __name__ == "__main__":
    root = Tree(10)
    root.left = Tree(5)
    root.right = Tree(15)
    root.left.left = Tree(3)
    root.left.right = Tree(7)
    root.right.right = Tree(18)
    root.right.right.right = Tree(19)

    print(root.isBalanced(root))