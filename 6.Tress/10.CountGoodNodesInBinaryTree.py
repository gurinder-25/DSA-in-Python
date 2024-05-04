class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

def goodNodes(root):
    def dfs(root, maxVal):
        if not root:
            return 0
        res = 1 if root.val>=maxVal else 0
        maxVal = max(root.val, maxVal)
        res += dfs(root.left, maxVal)
        res += dfs(root.right, maxVal)
        return res
    return dfs(root, root.val)

root = TreeNode(3)
root.left = TreeNode(1)
root.right = TreeNode(4)
root.left.left = TreeNode(3)
root.right.left = TreeNode(1)
root.right.right = TreeNode(5)
print(goodNodes(root))