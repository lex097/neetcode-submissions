# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def height(node):
            if not node:
                return 0
            return 1 + max(height(node.left), height(node.right))
        if not root:
            return 0
        if not root.left or not root.right:
            if not root.left:
                return max(height(root.left) + height(root.right), self.diameterOfBinaryTree(root.right))
            else:
                return max(height(root.left) + height(root.right), self.diameterOfBinaryTree(root.left))

        return height(root.left) + height(root.right)