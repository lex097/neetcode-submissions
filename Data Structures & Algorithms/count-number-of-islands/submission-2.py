class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        seen = set()
        islands = 0
        def dfs(r, c):
            #base case
            if ((r, c) in seen) or (r >= len(grid)) or (c >= len(grid[0])) or (r < 0) or (c < 0) or (grid[r][c] == "0"):
                return False
            seen.add((r, c))

            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

            return True
        
        for row in range(0, len(grid)):
            for column in range(0, len(grid[0])):
                if dfs(row, column):
                    islands = islands + 1
        return islands
