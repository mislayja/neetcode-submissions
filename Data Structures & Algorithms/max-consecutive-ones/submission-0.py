class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        total = 0
        curr = 0
        for num in nums:
            if num:
                curr+=1
                total=max(total,curr)
            else:
                curr = 0

        return total
        