# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        self.lca = None
        def search(node, p, q):
            if (node.val == p.val) or (node.val == q.val):
                self.lca = node
                return
            elif (node.val < max(p.val, q.val)) and (node.val > min(p.val, q.val)):
                self.lca = node
                return
            
            if (node.val > p.val) and (node.val > q.val):
                search(node.left, p, q)
            else:
                search(node.right, p, q)
        search(root, p, q)
        return self.lca