import collections

class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right


def rightSideView(root):
    res = []
    q = collections.deque([root])

    while q:
        rightSide = None
        qLen = len(q)

        for i in range(qLen):
            node = q.popleft()
            if node:
                rightSide = node
                q.append(node.left)
                q.append(node.right)
        if rightSide:
            res.append(rightSide.val)
    return res

root = TreeNode(1)
root.left = TreeNode(2)
root.left.right = TreeNode(5)
root.right = TreeNode(3)
root.right.right = TreeNode(4)
print(rightSideView(root))