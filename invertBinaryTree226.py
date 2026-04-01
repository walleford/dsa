def invert_tree(node):
    if not node:
        return
    sub = node.left
    node.left = node.right
    node.right = sub
    invert_tree(node.left)
    invert_tree(node.right)
    return node