class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not intervals:
            return [newInterval]
        check = 0
        for i in range(len(intervals)):
            if intervals[i][0] > newInterval[0]:
                intervals.insert(i, newInterval)
                break

            if i == (len(intervals) - 1):
                intervals.append(newInterval)
                break
            
            if intervals[i][0] <= newInterval[0] and intervals[i + 1][0] > newInterval[0]:
                intervals.insert(i + 1, newInterval)
                check = i
                break
        while (check + 1 < len(intervals)) and intervals[check][1] >= intervals[check + 1][0]:
            intervals[check][1] = max(intervals[check][1], intervals[check + 1][1])
            del intervals[check + 1]
        return intervals
        


