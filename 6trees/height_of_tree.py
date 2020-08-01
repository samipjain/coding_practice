class Tree:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
    '''
            10
        5       15
    3       7       18
    '''
    def height(self, root):
        if root is None:
            return 0
        lheight = self.height(root.left)
        rheight = self.height(root.right)

        return lheight+1 if lheight > rheight else rheight+1
    

if __name__ == "__main__":
    root = Tree(10)
    root.left = Tree(5)
    root.right = Tree(15)
    root.left.left = Tree(3)
    root.left.right = Tree(7)
    root.right.right = Tree(18)
    root.right.right.right = Tree(19)

    print(root.height(root))
