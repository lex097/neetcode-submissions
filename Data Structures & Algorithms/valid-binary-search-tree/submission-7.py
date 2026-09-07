# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right



class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        self.isBST = True
        #beMoreThan -> maximized, beLessThan -> minimized
        def dfs(node, beMoreThan , beLessThan):
            if not node:
                return
            if node.val <= beMoreThan or node.val >= beLessThan:
                self.isBST = False
                return
            dfs(node.left, beMoreThan, min(node.val, beLessThan))
            dfs(node.right, max(node.val, beMoreThan), beLessThan)
        dfs(root, -float('inf'), float('inf'))
        return self.isBST