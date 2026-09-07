# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        self.ret = True
        def dfs(nodeP, nodeQ):
            if (nodeP and not nodeQ) or (nodeQ and not nodeP):
                self.ret = False
                return
            if (not nodeP and not nodeQ):
                return

            if (nodeP.val != nodeQ.val):
                self.ret = False
                return
            
            dfs(nodeP.left, nodeQ.left)
            dfs(nodeP.right, nodeQ.right)

            return

        dfs(p, q)
        return self.ret