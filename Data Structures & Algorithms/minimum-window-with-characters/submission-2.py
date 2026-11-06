# from collections import defaultdict
# class Solution:
#     def minWindow(self, s: str, t: str) -> str:

#         def contains(check, has):
#             for char, count in has.items():
#                 if count> check[char]:
#                     return False
#             return True

#         # complicated because we need to find minumum :)
#         # sliding window left to right

#         # we just find the string, move left over till we cant no more, 
#         # then move right:
#         # we must match both characters not just 1, ie we must hash left side and compore right >= right count
#         need = {}
#         for char in t:
#             need[char] = 1+ need.get(char, 0)
        
#         # need is initialized
#         l = 0
#         r = 0
#         res = ""
#         curr =defaultdict(int)
#         while r<len(s):
#             # print(f"left={l}, right={r}, str={s[l:r]}, contains={contains(curr, need)}, curr={curr}, needs={need}, res={res}")
#             if contains(curr, need):
#                 # print(f"current res={res} with curr={curr}")
#                 # check if max is valid
#                 if not res or len(s[l:r]) < len(res): 
#                     res=s[l:r]
#                 # decrement left and move over try to find better string cutting it down.
#                 curr[s[l]]-=1
#                 l+=1
#             else:
#                 # add right and increment
#                 curr[s[r]]+=1
#                 r+=1
#         while contains(curr, need):
#             if not res or len(s[l:r]) < len(res):  res=s[l:r]
#             # need to check if we can cut down
#             curr[s[l]]-=1
#             l+=1
            
#         return res
        

# intuition is to replace contains() with a O(1) lookup tracking the # of uniques which we have found
# this replaces checking everything.  We'd track # we need with # we have, and update our haves when we see characters in need.
# copying code below:
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""

        countT, window = {}, {}
        for c in t:
            countT[c] = 1 + countT.get(c, 0)

        have, need = 0, len(countT)
        res, resLen = [-1, -1], float("infinity")
        l = 0
        for r in range(len(s)):
            c = s[r]
            window[c] = 1 + window.get(c, 0)

            if c in countT and window[c] == countT[c]:
                have += 1

            while have == need:
                if (r - l + 1) < resLen:
                    res = [l, r]
                    resLen = r - l + 1

                window[s[l]] -= 1
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have -= 1
                l += 1
        l, r = res
        return s[l : r + 1] if resLen != float("infinity") else ""
        
        