# class Solution:
#     def rob(self, nums: List[int]) -> int:
#         # ive done this exact problem already, I will try to impliment each and every iteration of it :)
        
#         def robem(num):
#             # num =index of current house, we should try to rob it, and compare with skipping it for neighboring house
#             if num>=len(nums):
#                 return 0
#             curr = nums[num] + robem(num+2)
#             alt = robem(num+1)
#             return max(curr, alt)

#         # we can either rob current house or house to right of it:
#         return robem(0)

#         # too slow:)

# class Solution:
#     def rob(self, nums: List[int]) -> int:
#         # lets memoize first
#         lookup=dict()

#         def robem(num):
#             if num>=len(nums):
#                 return 0
#             if num in lookup: return lookup[num]
#             curr = nums[num] + robem(num+2)
#             alt = robem(num+1)
#             m = max(curr, alt)
#             lookup[num] = m
#             return m

#         return robem(0)

# 3rd solution, build up array:
# class Solution:
#     def rob(self, nums: List[int]) -> int:
#         # start from 2 go till len(nums), start at 2, because first 2 houses no work can be done
#         if len(nums)==1: return nums[0]

#         nums[1]= max(nums[1],nums[0])  # nee to update nums because we could skip?
#         for i in range(2, len(nums)):
#             nums[i] = max(nums[i-1], nums[i]+nums[i-2])
#         return max(nums[-1], nums[-2])
            
# there is another solution which uses O(1) space and doesnt mutate the input
# this doesn't use any extra space since we're mutating input...



class Solution:
    def rob(self, nums: List[int]) -> int:
        # we want to track best result up to previous house
        # the best result from the house before that too
        rob1, rob2 = 0,0

        for num in nums:
            temp = max(num+rob1, rob2)
            # rob 1=1st house back
            rob1 = rob2
            rob2 = temp
        return rob2







