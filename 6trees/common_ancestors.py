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


def getAncestors(root, node1, node2):
    result = []
    print(node1.val, node2.val)
    result = getAncestorsHelper(root, node1, node2, result)
    
    return result
    
def getAncestorsHelper(root, node1, node2, result): # 3, 10, 5
    print('Root: ', root, "Result", result)
    # Base case
    if root is None:
        return
    
    # End case
    if node1.val == root.val or node2.val == root.val:
        return True       
    
    # Recursive function
    if getAncestorsHelper(root.left, node1, node2, result): # None, 10, 5, [4]
        if root.val not in result:
            result.append(root.val) # 4
    if getAncestorsHelper(root.right, node1, node2, result): # 5, 10, 5, [4]
        if root.val not in result:
            result.append(root.val) # 3
    
    return result
    

if __name__ == "__main__":
    tree = Tree(20)
    tree.left = Tree(8)
    tree.right = Tree(22)
    tree.left.left = Tree(4)
    tree.left.right = Tree(12)
    tree.left.right.left = Tree(10)
    tree.left.right.right = Tree(14)
    
    print(getAncestors(tree, tree.left.left, tree.left.right.right))