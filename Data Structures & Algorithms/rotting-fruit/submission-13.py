#bfs
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque()
        seen = set()
        self.fresh = 0
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        def addToQ(r, c):
            if (r >= len(grid)) or (c >= len(grid[0])) or (r < 0) or (c < 0) or ((r, c) in seen) or (grid[r][c] == 0):
                return
            seen.add((r,c))
            grid[r][c] = 2
            self.fresh = self.fresh - 1
            q.append((r, c))

        time = 0
        
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1:
                    self.fresh = self.fresh + 1
                if grid[row][col] == 2:
                    seen.add((row, col))
                    q.appendleft((row, col))
        if self.fresh == 0:
            return 0
        while q:
            for i in range(len(q)):
                r, c = q.popleft()
                for dr, dc in directions:
                    addToQ(r + dr, c + dc)
            time = time + 1
            if self.fresh == 0:
                break
        
        if self.fresh != 0:
            return -1
        return time
        

