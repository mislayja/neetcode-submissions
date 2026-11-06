class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # classic 2 pointer, we do swap...
        l = 0
        while nums[l]!=0:
            l+=1
        r = 0
        while r < len(nums):
            if nums[r]!=0 and r>l:
                # want to try shift it over
                nums[l] = nums[r]
                nums[r]=0
                while nums[l]!=0:
                    l+=1
            r+=1
        