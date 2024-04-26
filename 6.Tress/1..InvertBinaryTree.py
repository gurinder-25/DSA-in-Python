from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def invertTree(root):
    if not root:
        return

    tmp = root.left
    root.left = root.right
    root.right = tmp

    invertTree(root.left)
    invertTree(root.right)
    return root

def levelOrderTraversal(root):
    if not root:
        return []
    
    result = []
    queue = deque([root])

    while queue:
        node = queue.popleft()
        result.append(node.val)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

    return result

# Example usage
# Create a binary tree:
#        4
#       / \
#      2   7
#     / \ / \
#    1  3 6  9
root = TreeNode(4)
root.left = TreeNode(2)
root.right = TreeNode(7)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)
root.right.left = TreeNode(6)
root.right.right = TreeNode(9)

# Invert the binary tree
invertTree(root)

# Perform level order traversal and print the result
input_tree = levelOrderTraversal(root)
output_tree = levelOrderTraversal(root)
print("Input: root =", input_tree)
print("Output:", output_tree)
