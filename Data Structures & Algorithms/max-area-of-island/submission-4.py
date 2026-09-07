class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        seen = set()
        self.currArea = 0
        maxArea = float('-inf')
        def dfs(r, c):
            if (r >= len(grid)) or (c >= len(grid[0])) or (grid[r][c] == 0) or (r < 0) or (c < 0) or ((r, c) in seen):
                return
            seen.add((r, c))
            self.currArea = self.currArea + 1
            
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

            return
        
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                self.currArea = 0
                dfs(r, c)
                maxArea = max(maxArea, self.currArea)
        return maxArea