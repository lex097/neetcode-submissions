# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        self.lca = root
        def inTree(node, target):
            if not node:
                return False
            elif node.val == target:
                return True
            elif inTree(node.left, target) or inTree(node.right, target):
                return True
            else:
                return False
        def dfs(node, p, q):
            if not node:
                return
            if (node.val == p.val) or (node.val == q.val):
                self.lca = node
                return
            pInLeft = inTree(node.left, p.val)
            pInRight = inTree(node.right, p.val)
            qInLeft = inTree(node.left, q.val)
            qInRight = inTree(node.right, q.val)
            if (pInLeft and qInRight) or (pInRight and qInLeft):
                self.lca = node
                return
            dfs(node.left, p, q)
            dfs(node.right, p, q)
        dfs(root, p, q)
        return self.lca
