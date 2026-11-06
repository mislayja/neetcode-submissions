# class Solution:
#     def lengthOfLIS(self, nums: List[int]) -> int:
#         # we can memoize the indexes to see the longest subsequence
#         # this feels like a bottom up problem to memoize
#         # wait, but this is still O(n^2) because even if we memoize the computation, 
#         # we still need to look at subsequent values for larger ones. 
#         dp = [1]*len(nums)

#         for i in range(len(nums)-2,-1,-1):
#             # we need to iterate from i -> end now
#             long = 1
#             for j in range(i,len(nums)):
#                 # want to set long = max(long, dp[j])
#                 if nums[i] < nums[j]:
#                     long = max(long,1+dp[j])

#             dp[i]=long


#         return max(dp)

# this is optimal Solution
# we actually record the list of items that we've found, and when we find an item that's smaller than end, we replace it 
# we only need to update LIS, because once we get to point where 
from bisect import bisect_left
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = []
        dp.append(nums[0])

        LIS = 1
        for i in range(1, len(nums)):
            if dp[-1] < nums[i]:
                dp.append(nums[i])
                LIS += 1
                continue

            idx = bisect_left(dp, nums[i])
            dp[idx] = nums[i]

        return LIS