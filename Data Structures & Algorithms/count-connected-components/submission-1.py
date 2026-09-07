class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        ret = 0
        nodeMap = {i:[] for i in range(n)}
        unusedNodes = {i for i in range(n)}
        for i in edges:
            nodeMap[i[0]].append(i[1])
            nodeMap[i[1]].append(i[0])
        
        def search(node):
            if node not in unusedNodes:
                return

            unusedNodes.remove(node)

            for nd in nodeMap[node]:
                search(nd)
            
            return
        
        while unusedNodes:
            for i in unusedNodes:
                search(i)
                break
            ret = ret + 1
        return ret