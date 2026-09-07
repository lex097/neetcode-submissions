# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.nodes = 0

        def dfs(node, prevMax):
            if not node:
                return
            if node.val >= prevMax:
                self.nodes = self.nodes + 1
            dfs(node.left, max(node.val, prevMax))
            dfs(node.right, max(node.val, prevMax))

        dfs(root, -10000)
        return self.nodes
