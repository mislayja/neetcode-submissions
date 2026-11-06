class Solution:
    def validPalindrome(self, s: str) -> bool:
        # we can use 2 pointer and if it's not equal we can check whether we can skip left or right and if not return false. 
        # if we can we continue skip
        can_skip = True
        l,r = 0, len(s)-1

        while l <= r:
            # we have edge case where letter in middle could be incorrect
            if s[l] != s[r]:
                if not can_skip: return False

                # we need to check whether l+1 =r or r+1=l and l+1 !=r
                if s[l+1]==s[r]: # skip left here
                    l+=1
                    can_skip=False
                elif s[l]==s[r-1]:
                    r-=1
                    can_skip=False
                else: return False
            l+=1
            r-=1
        return True


# class Solution:
#     def validPalindrome(self, s: str) -> bool:
#         def is_palindrome(l, r):
#             while l < r:
#                 if s[l] != s[r]:
#                     return False
#                 l += 1
#                 r -= 1
#             return True

#         l, r = 0, len(s) - 1
#         while l < r:
#             if s[l] != s[r]:
#                 return (is_palindrome(l + 1, r) or
#                         is_palindrome(l, r - 1))
#             l += 1
#             r -= 1

#         return True