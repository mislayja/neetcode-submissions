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

class Solution:
    def rob(self, nums: List[int]) -> int:
        # lets memoize first
        lookup=dict()

        def robem(num):
            # num =index of current house, we should try to rob it, and compare with skipping it for neighboring house
            if num>=len(nums):
                return 0
            if num in lookup: return lookup[num]
            curr = nums[num] + robem(num+2)
            alt = robem(num+1)
            m = max(curr, alt)
            lookup[num] = m
            return m

        # we can either rob current house or house to right of it:
        return robem(0)

        # too slow:)