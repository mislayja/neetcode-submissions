class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        last = nums[0]
        idx = 1

        while idx < len(nums):
            if nums[idx] == last:
                nums.pop(idx)
            else:
                last = nums[idx]
                idx +=1
        
        return len(nums)
