"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        seen = {}
        def dfs(node):
            copy = Node(node.val)
            seen[node.val] = copy
            for i in node.neighbors:
                if i.val in seen:
                    copy.neighbors.append(seen[i.val])
                    continue
                copy.neighbors.append(dfs(i))
            
            return copy
        return dfs(node)