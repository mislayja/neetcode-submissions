# from collections import defaultdict
# class Solution:
#     def threeSum(self, nums: list[int]) -> list[list[int]]:
#         # this is somehow 2 pointer? huh?
#         # three pointer??
#         # brute force it?

#         # the i!=j, stuff just states we cant have 3 of same number

#         # we are looking the 
#         # we can sort to make finding the numbers easier?
        
#         # we fix one number look at others?
#         ret = []

#         # generate lookup, with value as index
#         lookup = defaultdict(list)
#         for idx, val in enumerate(nums):
#             lookup[val].append(idx)

#         # outer loop = fixed, translate into 2 sum problem...
#         for idx1, val1 in enumerate(nums):

#             for idx2 in range(idx1+1, len(nums)):  # when 
#                 val2= nums[idx2]
#                 target = -1* (val1+val2)
#                 for target_idx in lookup[target]:
#                     if target_idx not in (idx1, idx2) and sorted([val1,val2,target]) not in ret:
#                         # print(f"idx1:{idx1}, idx2:{idx2}, targetidx:{target_idx}")
#                         ret.append(sorted([val1,val2,target])) 
#         return ret
# TLE when we have large size array


from collections import defaultdict
class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        # need to fix first and actually use 2 pointers
        # also need to sort it
        nums.sort()
        ret=[]

        for idx1 in range(len(nums)):
            # skip duplicates, perf hack
            if idx1>0 and nums[idx1] == nums[idx1-1]:
                continue
            l = idx1+1
            r = len(nums)-1
            while l < r:
                # well either find our total here, or l will meet right and well exit
                target = (nums[idx1] + nums[l] + nums[r])
                if target ==0:
                    ret.append(sorted([nums[idx1], nums[l], nums[r]]))
                    l+=1
                    while nums[l] == nums[l-1] and l < r:
                        l += 1
                elif target>0: # >0 means we need to move right over
                    r-=1
                else:
                    l+=1
        return ret



        

        