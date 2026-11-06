"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        # this feels like a combinationn of previous in blind75. 
        # we want to try to be both greedy, keeping smallest meetings first, then re-iterating on the list 
        # theoretically, we could just increment += for all times, return max of these intervals
        times = [0]*1000000

        for interval in intervals:
            for idx in range(interval.start, interval.end):
                times[idx]+=1
        return max(times)
        