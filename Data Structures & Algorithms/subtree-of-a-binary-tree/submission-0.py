# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        self.isSub = False
        def isSame(node1, node2):
            if not node1 and not node2:
                return True
            if node1 and node2 and (node1.val == node2.val):
                return isSame(node1.left, node2.left) and isSame(node1.right, node2.right)
            else:
                return False
        def dfs(t1, t2):
            if not t1:
                return
            elif isSame(t1, t2):
                self.isSub = True
                return
            dfs(t1.left, t2)
            dfs(t1.right, t2)
        dfs(root, subRoot)
        return self.isSub