import math


def isValidBST(node, min=-math.inf, max=math.inf):
    # Empty trees are valid BSTs.
    if node == None:
        return True
    # The current node's value must be between low and high.
    if node.val <= min or node.val >= max:
        return False
    # The left and right subtree must also be valid.
    return (isValidBST(node.left, min, node.val)
            and
            isValidBST(node.right, node.val, max))
