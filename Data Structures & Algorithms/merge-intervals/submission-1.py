class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # this doesn't provide sorted intervals
        # i should sort by start time
        # O(nlog(n))
        intervals.sort(key=lambda x: x[0])

        # this is like extension of insert inverval, except we are now updating them in real time. 
        # thinking we can iterate on intervals, appending/updating last element in return list as we iterate on intervals
        ret = []
        for start, end  in intervals:
            if not ret: 
                ret.append([start,end])
            else:
                # we want to check for overlap now
                # want to check for overlap now
                if start <= ret[-1][1]:
                    ret[-1][0] = min(ret[-1][0], start)
                    ret[-1][1] = max(ret[-1][1], end)
                else:
                    ret.append([start,end])
        return ret
        # logic could be slightly updated, dont need start updating I dont think, 
        # we caould also combin the ret.append cases into singe if using logic inversion