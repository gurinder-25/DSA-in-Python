class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def insert(root, val):
    if not root:
        return TreeNode(val)
    if root.val>val:
        root.left = insert(root.left, val)
    elif root.val<val:
        root.right = insert(root.right, val)
    return root

def minValueNode(root):
    curr = root
    while curr and curr.left:
        curr = curr.left
    return curr

def remove(root, val):
    if not root:
        return None

    if root.val<val:
        root.right = remove(root.right, val)
    elif root.val>val:
        root.left = remove(root.left, val)
    else:
        if not root.right:
            return root.left
        elif not root.left:
            return root.right
        else:
            minNode = minValueNode(root.right)
            root.val = minNode.val
            root.right = remove(root.right, minNode.val)
    return root


def inorderTraversal(root):
    if root:
        inorderTraversal(root.left)
        print(root.val, end=" ")
        inorderTraversal(root.right)



# Create the BST
root = None
values = [4, 3, 2, 5, 6, 7]
for val in values:
    root = insert(root, val)

inorderTraversal(root)
print()

# Remove a value from the BST
remove_value = 4
root = remove(root, remove_value)
print(root.val)

inorderTraversal(root)
