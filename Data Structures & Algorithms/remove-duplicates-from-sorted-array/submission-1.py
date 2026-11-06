# class Solution:
#     def removeDuplicates(self, nums: List[int]) -> int:
        
#         last = nums[0]
#         idx = 1

#         while idx < len(nums):
#             if nums[idx] == last:
#                 nums.pop(idx)
#             else:
#                 last = nums[idx]
#                 idx +=1
        
#         return len(nums)


# copied from LC solutions:
class Solution:
    def removeDuplicates(self, nums):
        if not nums:  # Handle empty list case
            return 0

        j = 0  # Pointer for the position of unique elements
        for i in range(1, len(nums)):
            if nums[j] != nums[i]:
                j += 1  # Move to the next position for unique element
                nums[j] = nums[i]  # Assign the unique element

        return j + 1  # Return the length of the list with unique elements