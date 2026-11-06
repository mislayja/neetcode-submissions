# class Solution:
#     def countBits(self, n: int) -> List[int]:
#         # i've seen this already, we can memoize the numbers below this using bitmasks :)
#         # but that's kinda crazy for an easy solution :)
#         mem = [0]*(n+1)

#         total = []

#         for idx in range(n+1):
#             mem[idx] = mem[idx>>1] + (idx&1)
#             total.append(mem[idx])
#         return total

# we can also use standard libries :)
class Solution:
    def countBits(self, n: int) -> List[int]:
        return [bin(k).count('1') for k in range(n+1)]