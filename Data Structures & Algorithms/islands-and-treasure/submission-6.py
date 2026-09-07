#search from treasure

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        q = deque()
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        def bfs(r, c):
            q.appendleft((r, c))
            seen = set()
            dist = 0
            while q:
                for i in range(len(q)):
                    row, col = q.popleft()
                    seen.add((row, col))
                    for dr, dc in directions:
                        if (row + dr >= len(grid)) or (col + dc >= len(grid[0])) or (row + dr < 0) or (col + dc < 0) or (grid[row + dr][col+dc] == -1) or ((row + dr, col + dc) in seen):
                            continue
                        q.append((row + dr, col + dc))
                    grid[row][col] = min(grid[row][col], dist)

                dist = dist + 1
            return

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 0:
                    bfs(r, c)
        return

    
