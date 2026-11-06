
from functools import reduce
import operator
from itertools import combinations

class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        #Hint Nudge

# Notice the small constraint on `nums.length` ($n \le 12$). Since an array of length $n$ has $2^n$ subsets, $2^{12} = 4096$, which is small enough to consider examining all subsets.
        # ok we need to iterate 
        def xor_array_reduce(arr):
            return reduce(operator.xor, arr, 0)

        total = 0
        for size in range(1, len(nums)+1):
            for combo in combinations(nums,size):
                total+=xor_array_reduce(combo)

        return total
