class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # we can memoize the indexes to see the longest subsequence
        # this feels like a bottom up problem to memoize
        # wait, but this is still O(n^2) because even if we memoize the computation, 
        # we still need to look at subsequent values for larger ones. 
        dp = [1]*len(nums)

        for i in range(len(nums)-2,-1,-1):
            # we need to iterate from i -> end now
            long = 1
            for j in range(i,len(nums)):
                # want to set long = max(long, dp[j])
                if nums[i] < nums[j]:
                    long = max(long,1+dp[j])

            dp[i]=long


        return max(dp)