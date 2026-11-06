class Solution:
    def findMin(self, nums: List[int]) -> int:
        # binary search because log(n) time

        # can we simply just binary search for it?
        # not exatcly because the minumum could very well be at the end? 
        # can we simply duplicate and binary search on that? 
        # if we repeat it, we'll have a full array in the sub array
        # guess im supposed to rip a bst anyways:)
        l = 0
        r = len(nums)-1

        while l < r:
            left = nums[l]
            right = nums[r]
            m = (r+l)//2
            mid = nums[m]

            # print(f"left={left}, mid={mid}, right={right}")

            # 6 total cases with l, r, mid?
            
            if left <= mid <= right:
                # move to left
                r = m-1
            elif right<=left and mid>right:
                # shift up becuase mid>right
                l = m+1
            else: # case when right is
                r = m
        
        return nums[l]