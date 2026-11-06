

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        res = -1
        l = 0
        r = len(nums)-1

        while l<=r:
            right = nums[r]
            left = nums[l]
            m = (l+r)//2
            mid = nums[m]
            if mid == target: return m

            if left <= mid: # right sorted portion
                if target> mid or target < left:
                    # we are looking at correctly sorted area, if our desired value is smaller than smallest, we know it should be in right side
                    # similarly if our want is bigger than biggest in this section, we need to look right. 
                    l=m+1
                else:
                    r=m-1
            else:
                if target < mid or target > right:
                    # essentially inverse of above
                    # if our mid value is less than target, we look left necause it could be a couple spaces to left of mid...
                    # if our target is greater than our biggest value here we look left because it was rotated out. 
                    r = m-1
                else:
                    l = m+1
            # print(f"l={left}, mid={mid}, right={right}")

            

        # print(f"ending bst with l={l}, left={nums[l]}")
        return -1
        

 

