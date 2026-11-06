class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums) # 0 not good default because negative allowed
        low, high = 1,1
        for num in nums: 
            if num == 0:
                low, high =1,1
            else:
                low_prod, high_prod = low*num, high*num
                low = min(low_prod, high_prod)
                high = max(low_prod, high_prod)
                res = max(res, high)

        return res

        