class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        ret = []
        i = 1
        curr = intervals[0]
        print(intervals)
        while i < len(intervals):
            if curr[1] < intervals[i][0]:
                ret.append(curr[:])
                curr = intervals[i]
            elif curr[0] > intervals[i][1]:
                ret.append(intervals[i])
            else:
                curr = [min(curr[0], intervals[i][0]), max(curr[1], intervals[i][1])]

            i = i + 1
        ret.append(curr)
        return ret
