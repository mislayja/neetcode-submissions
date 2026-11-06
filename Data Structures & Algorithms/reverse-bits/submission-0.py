class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        for i in range(32):
            bit = (n>>i)&1          # determine if current bit equals 1 or 0
            res += (bit << (31-i))  # tries to set it in result using +=
        return res