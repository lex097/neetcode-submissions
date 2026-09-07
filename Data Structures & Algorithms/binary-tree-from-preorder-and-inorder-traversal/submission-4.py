# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inorderIndexFor = dict()
        for index,element in enumerate(inorder):
            inorderIndexFor[element] = index
        preOrderListIndex = 0
        def dfs(leftBound, rightBound):
            nonlocal preOrderListIndex

            if leftBound > rightBound:
                return None

            newRootVal = preorder[preOrderListIndex]
            newRoot = TreeNode(newRootVal)

            preOrderListIndex += 1


            newRoot.left = dfs(leftBound, inorderIndexFor[newRootVal]-1)
            newRoot.right = dfs(inorderIndexFor[newRootVal]+1, rightBound)


            return newRoot
            


        return dfs(0, len(preorder)-1)
