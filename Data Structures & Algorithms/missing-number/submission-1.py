# class Solution:
#     def missingNumber(self, nums: List[int]) -> int:
#         res = 0
#         for val in range(len(nums)+1):
#             res ^=val
#         for val in nums: 
#             res^=val
#         return res

# math solution now
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)+1
        return (n*(n-1)//2) - sum(nums)
        