class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        # they just contain 1-n, not ordered 1-n


        missing = (set(range(1,len(nums)+1)) - set(nums)).pop()
        d = {}
        for num in nums:
            if num in d:
                return [num, missing]
            else:
                d[num]=True