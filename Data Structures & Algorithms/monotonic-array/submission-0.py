class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:

        increasing = None
        curr = nums[0]
        for val in nums[1:]:
            if increasing == None:
                if val < curr: increasing = False
                elif val > curr: increasing = True
            if increasing and val < curr: return False
            elif increasing == False and val > curr: return False
            curr = val
        return True