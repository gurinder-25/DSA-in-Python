class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def inorder(root):
    if not root:
        return
    inorder(root.left)
    print(root.val, end=" ")
    inorder(root.right)

def preorder(root):
    if not root:
        return
    print(root.val, end=" ")
    preorder(root.left)
    preorder(root.right)

def postorder(root):
    if not root:
        return
    postorder(root.left)
    postorder(root.right)
    print(root.val, end=" ")



t = TreeNode(4)
t.left = TreeNode(3)
t.left.left = TreeNode(2)
t.right = TreeNode(6)
t.right.left = TreeNode(5)
t.right.right = TreeNode(7)
inorder(t)
print()
preorder(t)
print()
postorder(t)