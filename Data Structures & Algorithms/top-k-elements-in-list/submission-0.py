from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # sort iterate on that
        # there seems like a better way though. 
        # insert into dict-> sort that.. would have better time complexity performance
        a = defaultdict(int)
        for num in nums:
            a[num]+=1
        # print(a.items())
        return [ ans[0] for idx, ans in enumerate(sorted(a.items(), reverse=True, key = lambda k: k[1] )) if idx < k]

        # we couldve used min heap here to reduce further...
        # buketing ie using index as frequency is better solution?
        # use frequency map solution since O(n), then building array, then iterating on it
        #  3 passes, but still O(n) :)