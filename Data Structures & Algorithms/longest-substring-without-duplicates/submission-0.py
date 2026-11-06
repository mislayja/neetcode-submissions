# class Solution:
#     def lengthOfLongestSubstring(self, s: str) -> int:
#         # is this just 1 pass with create/clear dictionary over and over? 
#         # is in vs is not in?
#         d = {}
#         l = 0
#         curr = 0

#         i = 0

#         while i < len(s):
#             char = s[i]
#             if char not in d:
#                 d[char]=i
#                 curr+=1
#                 l = max(l, curr)
#                 i+=1
#             else:
#                 # reset i to 1+where it was last seen in the map
#                 i = d[char]+1
#                 d.clear()
#                 curr = 0

#         return l

# my solution was ungodly slow, what can we do to speed this up? 
# my guess would be to not need to repeat when we see duplicates towards later half

# is this a l/r pointer problem, move left/right until we see duplicate
# the ideal is the shrinking method... removing the elements as needed till we see repeat

# class Solution:
#     def lengthOfLongestSubstring(self, s: str) -> int:

#         l = r = 0
#         big = 0
#         found = set()

#         while r < len(s):
#             char = s[r]
#             if char not in found:
#                 # print(f"adding char:{char} to set:{found}")
#                 found.add(char)
#             else:
#                 # print(f"need to remove char:{char}, with set={found}")
#                 # need to move left till we find what l was pointing to
#                 while s[l] != char:
#                     found.remove(s[l])
#                     l+=1
#                 l+=1
                
#             big = max(big, len(found))
#             r+=1
                

#         return big



# finally taking from the neetcode solution, we can instead remove while our char is in the set, then simply re add it:
# ok performance is essentially the same, idk whats goiing on here :)
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l_ptr = 0
        existing_string = set()
        global_max = 0
        for r_ptr in range(len(s)):
            while s[r_ptr] in existing_string:
                existing_string.remove(s[l_ptr])
                l_ptr += 1
            existing_string.add(s[r_ptr])
            global_max = max(global_max, len(existing_string))
        return global_max