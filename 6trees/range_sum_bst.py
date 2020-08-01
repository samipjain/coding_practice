class Tree:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
    
    def rangeSum(self, root, L, R):
        return self.inorder(root, 0, L, R)

    def inorder(self, root, result, L, R):
        if root:
            result = self.inorder(root.left, result, L, R)

            if root.val >= L and root.val <= R:
                result += root.val

            result = self.inorder(root.right, result, L, R)

        return result

    def rangeSumIteration(self, root, L, R):
        result = 0
        stack = [root]

        while stack:
            node = stack.pop()

            if node.val >= L and node.val <= R:
                result += node.val
            if node.left is not None:
                stack.append(node.left)
            if node.right is not None:
                stack.append(node.right)

        return result

if __name__ == "__main__":
    root = Tree(10)
    root.left = Tree(5)
    root.right = Tree(15)
    root.left.left = Tree(3)
    root.left.right = Tree(7)
    root.right.right = Tree(18)

    L, R = 7, 15
    print(root.rangeSum(root, L, R))

    print(root.rangeSumIteration(root, L, R))
