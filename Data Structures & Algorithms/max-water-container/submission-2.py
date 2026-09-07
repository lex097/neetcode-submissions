class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        currMax = 0
        while l < r:
            area = min(heights[l], heights[r]) * (r - l)
            currMax = max(currMax, area)
            if heights[l] > heights[r]:
                r = r-1
                continue
            if heights[l] < heights[r]:
                l = l+1
                continue
            if heights[l] == heights[r]:
                l = l+1
                continue
        return currMax