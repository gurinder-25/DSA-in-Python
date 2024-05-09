class Treenode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None 

def maxPathSum(root):
    res = [root.val]

    def dfs(root):
        if not root:
            return 0
        leftmax = dfs(root.left)
        rightmax = dfs(root.right)
        leftmax = max(leftmax, 0)
        rightmax = max(rightmax, 0)
        res[0] = max(res[0], root.val + leftmax + rightmax)
        return root.val + max(leftmax, rightmax)

    dfs(root)
    return res[0]

root = Treenode(1)
root.left = Treenode(2)
root.right = Treenode(3)
print(maxPathSum(root))