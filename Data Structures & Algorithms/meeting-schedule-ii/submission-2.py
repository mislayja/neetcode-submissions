# """
# Definition of Interval:
# class Interval(object):
#     def __init__(self, start, end):
#         self.start = start
#         self.end = end
# """

# class Solution:
#     def minMeetingRooms(self, intervals: List[Interval]) -> int:
#         # this feels like a combinationn of previous in blind75. 
#         # we want to try to be both greedy, keeping smallest meetings first, then re-iterating on the list 
        
#         # theoretically, we could just increment += for all times, return max of these intervals
#         times = [0]*1000000

#         for interval in intervals:
#             for idx in range(interval.start, interval.end):
#                 times[idx]+=1
#         return max(times)
#         # not just theoretically, this is a valid solution, albeit slow.
#         # lets try the alternative greedy solution next, 
"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        # this can be simplified with 2 pointers:)

        
        times = []
        # we could just create sorted list of start+end and use stack rather than 2 pointers
        for interval in intervals:
            times.append([interval.start, True])
            times.append([interval.end,False])


        times.sort(key = lambda x: (x[0],x[1]))
        count = 0
        res = 0
        for time, start in times:
            if start:
                count+=1
                res = max(res, count)
            else:
                count-=1

        return res