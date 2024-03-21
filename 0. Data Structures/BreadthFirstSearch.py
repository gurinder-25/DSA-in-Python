from collections import deque

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def bfs(root):
    queue = deque()

    if root:
        queue.append(root)
    level = 0
    while len(queue)>0:
        print("Level: ", level)
        for i in range(len(queue)):
            curr = queue.popleft()
            print(curr.val)
            if curr.left:
                queue.append(curr.left)
            if curr.right:
                queue.append(curr.right)
        level+=1


t = TreeNode(4)
t.left = TreeNode(3)
t.left.left = TreeNode(2)
t.right = TreeNode(6)
t.right.left = TreeNode(5)
t.right.right = TreeNode(7)
bfs(t)