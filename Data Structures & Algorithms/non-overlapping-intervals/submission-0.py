class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # this was a greedy Solution
        # sort by start, take the smallest one each time, remove largest, track next highest
        
        # O(n*log(n))
        intervals.sort(key = lambda x: x[0])

        remove=0
        big = intervals[0][0]
        for interval in intervals[1:]:
            if interval[0]<big:
                # overlapping
                remove+=1
            big = max(big, interval[1])

        return remove
        