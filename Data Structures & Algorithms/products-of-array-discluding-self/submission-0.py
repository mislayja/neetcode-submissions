class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # so i've already solved this... we just iterate through the list multiplying by the values over and over
        # I think there were edge cases if 0 is in the array

        zero_count = 0 
        product = 1
        zero_idx = 0

        for idx, val in enumerate(nums):
            if val == 0:
                zero_count +=1
                zero_idx = idx
            else:
                product *= val
        
        if zero_count >=2:
            return [0]*len(nums)
        elif zero_count >0:
            return ([0]*(zero_idx))+[product]+[0]*(len(nums)-zero_idx-1)
        else:
            return [int(product/val) for val in nums]

        