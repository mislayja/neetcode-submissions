class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        m = 0

        # we dont actually need the dict here:)
        for num in nums:
            if num-1 not in nums:
                # do right ways lookup
                curr = 1
                x = num+1
                while x in nums:
                    curr+=1
                    x+=1

                m = max(m, curr)



        return m
        