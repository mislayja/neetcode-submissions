# from collections import defaultdict

# class Solution:



#     def characterReplacement(self, s: str, k: int) -> int:
        
#         def get_num_replacements(arr):
#             # find max character
#             return sum(arr) - max(arr)

#         # we need to find a window where the char!= most common <=k.
#         # move right if we find it we pass, next iteration move left
#         # max = use array, brute force search it...
#         chars = [0]*26

#         l = 0
#         r = k
#         longest=k

#         for idx in range(k):
#             chars[ord(s[idx])-65] +=1
        
#         # now we iterate while k<len
#         while r<len(s):
#             # print(f"l={l},r={r},get_num_replacements(chars)={get_num_replacements(chars)}")
#             if get_num_replacements(chars) <=k:
#                 longest = max(longest, r-l)
#                 # lets move right over now
#                 chars[ord(s[r])-65]+=1
#                 r+=1           
#             else:
#                 # remove left +increment
#                 chars[ord(s[l])-65]-=1
#                 l+=1
#         # edge case, last character needs to be counted but we incremented past it:)
#         if get_num_replacements(chars) <=k:
#             longest = max(longest, r-l)
#         return longest

# we dont need to sort to get max :)
# this way avoids duplicated checks, and also just uses dictionary:
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        res = 0

        l = 0
        maxf = 0
        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)
            maxf = max(maxf, count[s[r]])

            while (r - l + 1) - maxf > k:
                count[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1)

        return res