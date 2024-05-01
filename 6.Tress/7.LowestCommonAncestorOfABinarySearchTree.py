class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def lowestCommonAncestor(root, p, q):
    cur = root
    while cur:
        if p.val>cur.val and q.val>cur.val:
            cur = cur.right
        elif p.val<cur.val and q.val<cur.val:
            cur = cur.left
        else:
            return cur




root = TreeNode(6)
root.left = TreeNode(2)
root.right = TreeNode(8)
root.left.left = TreeNode(0)
root.left.right = TreeNode(4)
root.left.right.left = TreeNode(3)
root.left.right.right = TreeNode(5)
root.right.left = TreeNode(7)
root.right.right = TreeNode(9)

print(lowestCommonAncestor(root, root.left, root.right).val)