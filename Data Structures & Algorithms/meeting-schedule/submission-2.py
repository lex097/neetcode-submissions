"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key = lambda i : i.start)
        
        prev_end = - float('inf')
        for i in intervals:
            if i.start < prev_end:
                return False
            prev_end = i.end
        return True