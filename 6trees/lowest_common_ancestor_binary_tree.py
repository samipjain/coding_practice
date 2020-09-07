#' binary trees
# a binary tree where each parent node has information about its
# two child nodes and nothing else, no parent pointers
# just a simple binary tree, not a search tree, not complete, not balanced

#.    3
#.  4.  5
#.10  9

# input as two nodes -> [ 4,5]
#  output -> [3]
# input -> [10, 9]
# output -> [3,4] in any order

# Return ALL common ancestors of the two nodes

# Input [4,9] => [4,3]

# 3 => null

# [10, 5] => [4, 3]
#    3
#   4 5
   
class Tree:
    def __init__(self, v):
        self.val = v
        self.left = None
        self.right = None


def lowestCommonAncestor(root, node1, node2):
    # Base case
    if root is None:
        return
    
    # End case
    if node1 == root.val or node2 == root.val:
        return root
    
    # Recursive function
    left_lca = lowestCommonAncestor(root.left, node1, node2)
    right_lca = lowestCommonAncestor(root.right, node1, node2)
    
    if left_lca is not None and right_lca is not None:
        return root
    else:
        return left_lca if left_lca is not None else right_lca

if __name__ == "__main__":
    tree = Tree(20)
    tree.left = Tree(8)
    tree.right = Tree(22)
    tree.left.left = Tree(4)
    tree.left.right = Tree(12)
    tree.left.right.left = Tree(10)
    tree.left.right.right = Tree(14)
    
    print(lowestCommonAncestor(tree, tree.left.left.val, tree.right.val).val)