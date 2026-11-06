# class NumArray:

#     def __init__(self, nums: List[int]):
#         self.nums = nums

#     def sumRange(self, left: int, right: int) -> int:
#         return sum(self.nums[left:right+1])
class NumArray:

    def __init__(self, nums: List[int]):
        # lets build prefix array here
        self.prefix = [0]*(len(nums)+1)
        for num in range(len(nums)):
            self.prefix[num+1] = nums[num]+self.prefix[num]

    def sumRange(self, left: int, right: int) -> int:
        return (self.prefix[right+1]-self.prefix[left])

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)