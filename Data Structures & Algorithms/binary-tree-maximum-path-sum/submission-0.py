# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.maxsum = root.val

        def dfs(node):
            if not node:
                return 0

            leftMax = max(dfs(node.left), 0)
            rightMax = max(dfs(node.right), 0)
            self.maxsum = max(self.maxsum, node.val + leftMax + rightMax, node.val + max(leftMax, rightMax))
            return node.val + max(leftMax, rightMax)
        dfs(root)
        return self.maxsum