class Tree:
    def __init__(self, v):
        self.val = v
        self.left = None
        self.right = None


def getAncestors(root, node):
    return getAncestorsHelper(root, node, [])

def getAncestorsHelper(root, node, result):
    if root is None:
        return
    
    if root.val == node:
        return True
    
    if getAncestorsHelper(root.left, node, result) or getAncestorsHelper(root.right, node, result):
        if node not in result:
            result.append(node)
        result.append(root.val)

    return result
    

if __name__ == "__main__":
    # tree = Tree(3)
    # tree.left = Tree(4)
    # tree.right = Tree(5)
    # tree.left.left = Tree(10)
    # tree.left.right = Tree(9)

    # print("Ancestor of ", tree.val, ": ", getAncestors(tree, tree.val))
    # print("Ancestor of ", tree.left.val, ": ", getAncestors(tree, tree.left.val))
    # print("Ancestor of ", tree.right.val, ": ", getAncestors(tree, tree.right.val))
    # print("Ancestor of ", tree.left.left.val, ": ", getAncestors(tree, tree.left.left.val))
    # print("Ancestor of ", tree.left.right.val, ": ", getAncestors(tree, tree.left.right.val))

    tree = Tree(20)
    tree.left = Tree(8)
    tree.right = Tree(22)
    tree.left.left = Tree(4)
    tree.left.right = Tree(12)
    tree.left.right.left = Tree(10)
    tree.left.right.right = Tree(14)
    
    print("Ancestor of ", tree.val, ": ", getAncestors(tree, tree.val))
    print("Ancestor of ", tree.left.val, ": ", getAncestors(tree, tree.left.val))
    print("Ancestor of ", tree.right.val, ": ", getAncestors(tree, tree.right.val))
    print("Ancestor of ", tree.left.left.val, ": ", getAncestors(tree, tree.left.left.val))
    print("Ancestor of ", tree.left.right.val, ": ", getAncestors(tree, tree.left.right.val))
    print("Ancestor of ", tree.left.right.left.val, ": ", getAncestors(tree, tree.left.right.left.val))
    print("Ancestor of ", tree.left.right.right.val, ": ", getAncestors(tree, tree.left.right.right.val))