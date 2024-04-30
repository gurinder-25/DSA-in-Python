class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def isSubtree(root, subRoot):
    if not subRoot: return True
    if not root: return False

    def isSameTree(p, q):
        if not p and not q:
            return True
        if not p or not q or (p.val!=q.val):
            return False
        return (isSameTree(p.left, q.left) and isSameTree(p.right, q.right))

    if isSameTree(root, subRoot):
        return True
    return (isSubtree(root.left, subRoot) or isSubtree(root.right, subRoot))





p = TreeNode(3)
p.left = TreeNode(4)
p.right = TreeNode(5)
p.left.left = TreeNode(1)
p.left.right = TreeNode(2)


q = TreeNode(4)
q.left = TreeNode(1)
q.right = TreeNode(2)

print(isSubtree(p, q))