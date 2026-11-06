class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # let's jut keep track of max we can reach and iterate across array to see if we get stuck
        m = 0

        for idx,num in enumerate(nums):
            if m<idx: return False
            m = max(idx+num, m)
            # print(f"m={m}, current={num}")
        
        if m<(len(nums)-1): return False

        return True
        