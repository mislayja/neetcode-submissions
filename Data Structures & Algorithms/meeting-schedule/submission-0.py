"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        # this feels like a simple sort+iterate
        # im wondering if there is a better solution here?
        intervals.sort(key = lambda x: x.start)

        prev_end = 0
        for interval in intervals:
            if prev_end > interval.start: return False
            prev_end = interval.end


        return True
