class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        ret = 0
        intervals.sort()

        print(intervals)
        prev_end = float('-inf')
        for i in intervals:
            start, end = i[0], i[1]

            if start >= prev_end:
                prev_end = end
            else:
                ret += 1
                prev_end = min(end, prev_end)
        



        return ret