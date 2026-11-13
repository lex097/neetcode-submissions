class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        self.ret = 0
        self.currSize = 0

        r_size = len(grid)
        c_size = len(grid[0])
        seen = set()
        def dfs(r, c, size):
            if (r, c) in seen:
                return
            seen.add((r, c))
            if r < 0 or r >= r_size or c < 0 or c >= c_size or grid[r][c] == 0:
                return
            self.currSize += 1
            self.ret = max(self.ret, self.currSize)

            dfs(r + 1, c, self.currSize)
            dfs(r, c + 1, self.currSize)
            dfs(r - 1, c, self.currSize)
            dfs(r, c - 1, self.currSize)
            return

        
        for r in range(r_size):
            for c in range(c_size):
                self.currSize = 0
                dfs(r, c, 0)
        return self.ret
        
        