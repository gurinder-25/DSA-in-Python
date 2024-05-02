import collections

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def levelOrder(root):
    res = []
    queue = collections.deque()
    if root:
        queue.append(root)
    level = 0
    while len(queue)>0:
        l1 = []
        for i in range(len(queue)):
            cur = queue.popleft()
            l1.append(cur.val)
            if cur.left:
                queue.append(cur.left)
            if cur.right:
                queue.append(cur.right)
        if l1:
            res.append(l1)
        level+=1
    return res


root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

print(levelOrder(root))