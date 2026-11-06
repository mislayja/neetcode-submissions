class Solution:
    def rob_normal(self, nums: List[int]) -> int:
        # we want to track best result up to previous house
        # the best result from the house before that too
        rob1, rob2 = 0,0

        for num in nums:
            temp = max(num+rob1, rob2)
            # rob 1=1st house back
            rob1 = rob2
            rob2 = temp
        return rob2

    def rob(self, nums: List[int]) -> int:
        # same algorithm except we need to track whether the node we chose was node 0 or 1, or none
        # we need to check the further item after the fact with idx+=...
        # we just need to know whether first house was robbed?  to know whether we can/cannot rob last house


        # the solution to this is just breaking up the problem into smaller problems
        return max(nums[0], self.rob_normal(nums[1:]), self.rob_normal(nums[:-1]))