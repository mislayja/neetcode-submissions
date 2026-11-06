class Solution:
    def getSum(self, a: int, b: int) -> int:
        # a can be negative????
        # let's just perform operation on all 32 bits :)
        res = 0
        carryover = 0
        mask = 0xFFFFFFFF

        for idx in range(32):
            a_val = (a>>idx)&1
            b_val = (b>>idx)&1
            curr = a_val ^ b_val ^ carryover
            res = res | (curr << idx)
            carryover = a_val&b_val or b_val&carryover or a_val&carryover
        if res > 0x7FFFFFFF:
            res = ~(res ^ mask)
        return res

# class Solution:
#     def getSum(self, a: int, b: int) -> int:
#         while (b!=0):
#             temp = (a&b)<<1
#             a = a^b
#             b = temp
#         return a

# class Solution:
#     def getSum(self, a: int, b: int) -> int:
#         mask = 0xFFFFFFFF
#         max_int = 0x7FFFFFFF

#         while b != 0:
#             carry = (a & b) << 1
#             a = (a ^ b) & mask
#             b = carry & mask

#         return a if a <= max_int else ~(a ^ mask)