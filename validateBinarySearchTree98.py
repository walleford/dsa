def validate(node, min, max):
    # node.left must be less than node
    # node right must be greater than node
    # left/right must be BST as well
    min, max = node.val
    if node.left < node:
        validate(node.left, max, min)
        return True
    if node.right > node:
        validate(node.right, min, max)
        return True
    return False