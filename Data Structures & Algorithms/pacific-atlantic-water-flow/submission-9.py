class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pacific = set()
        atlantic = set()
        seen = set()
        def search(r, c, ocean, prevHeight):
            if (r < 0) or (c < 0) or (r >= len(heights)) or (c >= len(heights[0])) or ((r, c) in ocean) or (heights[r][c] < prevHeight):
                return
            ocean.add((r, c))

            search(r + 1, c, ocean, heights[r][c])
            search(r - 1, c, ocean, heights[r][c])
            search(r, c + 1, ocean, heights[r][c])
            search(r, c - 1, ocean, heights[r][c])
            return

        for r in range(len(heights)):
            search(r, 0, pacific, -float('inf'))
        for c in range(len(heights[0])):
            search(0, c, pacific, -float('inf'))
        
        # Start from Atlantic borders (bottom and right)
        for r in range(len(heights)):
            search(r, len(heights[0]) - 1, atlantic, -float('inf'))
        for c in range(len(heights[0])):
            search(len(heights) - 1, c, atlantic, -float('inf'))
        ret = []
        for i in pacific:
            if i in atlantic:
                r, c = i
                ret.append([r,c])
        return ret