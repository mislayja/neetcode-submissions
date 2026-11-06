class Solution:
    def validPalindrome(self, s: str) -> bool:
        # we can use 2 pointer and if it's not equal we can check whether we can skip left or right and if not return false. 
        # if we can we continue skip

        l,r = 0, len(s)-1
        def is_palindrome(left,right):
            while left <= right:
                if s[left]!=s[right]: return False
                left+=1
                right-=1
            return True
        
        while l <=r:
            if s[l]!=s[r]:
                return (is_palindrome(l+1,r) or is_palindrome(l,r-1))
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