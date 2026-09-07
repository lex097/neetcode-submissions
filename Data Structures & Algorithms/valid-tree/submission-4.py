class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        nodeMap = {}

        for i in range(n):
            nodeMap[i] = []

        for i in edges:
            nodeMap[i[0]].append(i[1])
            nodeMap[i[1]].append(i[0])
        print(nodeMap)
        cycle = set()

        def dfs(node, prevUsed):
            if node in cycle:
                return False
            cycle.add(node)
            
            for nd in nodeMap[node]:
                if nd == prevUsed:
                    continue
                if not dfs(nd, node):
                    return False
            return True

        if not dfs(0, -1):
            return False
        if len(cycle) == n:
            return True
        return False