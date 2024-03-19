class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def search(root, target):
    if not root:
        return False

    if target>root.val:
        return search(root.right, target)
    elif target<root.val:
        return search(root.left, target)
    else:
        return True


root = TreeNode(5)
root.right = TreeNode(6)
root.left = TreeNode(3)
root.left.left = TreeNode(2)
root.left.right = TreeNode(4)
root.right.right = TreeNode(7)


print(search(root, 3))
print(search(root, 7))