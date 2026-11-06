class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        # I think we can 1 pass this?
        for idx, val in enumerate(nums):
            if val != idx+1:
                return [val, idx+1]