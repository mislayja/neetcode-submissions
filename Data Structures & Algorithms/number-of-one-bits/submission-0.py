class Solution:
    def hammingWeight(self, n: int) -> int:
        # this is best performed while n >0, +=right bit....
        res = 0
        while n>0:
            res+=n&1
            n = n>>1
        return res