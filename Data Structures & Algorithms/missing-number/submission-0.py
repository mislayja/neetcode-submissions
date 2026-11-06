class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        res = 0
        for val in range(len(nums)+1):
            res ^=val
        for val in nums: 
            res^=val
        return res