# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        self.ret = None
        def dfs(node, p, q):
            
            if not node:
                return False

            l = dfs(node.left, p, q)
            r = dfs(node.right, p , q)

            if node.val == p or node.val == q:

                if l or r:
                    self.ret = node
                return True
            
            if l and r:
                self.ret = node
                return True
            


            return l or r
        dfs(root, p.val, q.val)

        return self.ret