class Tree:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
    
    def contains(self, root, value):
        if root != None:
            if root.val == value:
                return True
            if self.contains(root.left, value) or self.contains(root.right, value):
                return True
        return False
    
    # Faster
    def containsBST(self, root, value):
        if root != None:
            if root.val == value:
                return True
            elif value < root.val:
                return self.contains(root.left, value)
            else:
                return self.contains(root.right, value)
        return False

         
if __name__ == "__main__":
    root = Tree(10)
    root.left = Tree(5)
    root.right = Tree(12)
    root.left.left = Tree(3)
    root.left.right = Tree(8)

    print(root.contains(root, 8))

    print(root.containsBST(root, 18))