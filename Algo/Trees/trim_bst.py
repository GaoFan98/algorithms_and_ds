class Node:
    def __init__(self, data):
        self.val = data
        self.left = None
        self.right = None


def trim_bts(tree, min, max):
    if not tree:
        return False

    tree.left = trim_bts(tree.left, min, max)
    tree.right = trim_bts(tree.right, min, max)

    if min <= tree.val <= max:
        return tree

    if tree.val < min:
        return tree.right

    if tree.val > max:
        return tree.left
