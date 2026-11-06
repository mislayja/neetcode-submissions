class Solution:
    def getSum(self, a: int, b: int) -> int:
        # a can be negative????
        # let's just perform operation on all 32 bits :)
        res = 0
        carryover = 0
        for idx in range(32):
            a_val = (a>>idx)&1
            b_val = (b>>idx)&1
            curr = a_val ^ b_val ^ carryover
            res = res | (curr << idx)
            carryover = a_val&b_val or b_val&carryover or a_val&carryover
        return res