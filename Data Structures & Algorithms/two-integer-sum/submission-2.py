class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # use hash map, look for neighbor, if available return both idx, else insert next
        rl = {}
        for idx, item in enumerate(nums):
            need = target - item
            if need in rl:
                return [rl[need], idx ]
            
            rl[item] = idx 