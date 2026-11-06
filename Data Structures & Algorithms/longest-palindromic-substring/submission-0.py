class Solution:
    def longestPalindrome(self, s: str) -> str:
        # how is this dp. 
        dp={}
        res = ""
        def isPalandrome(l,r):
            while l<=r:
                if s[l] != s[r]: return False
                l+=1
                r-=1
            return True
        
        def recurse(l,r):
            # print(f"recurse,l={l},r={r},str={s[l:r+1]}")
            # we want to first verify l<=r 
            nonlocal res
            if l>r or (r-l+1) <= len(res): return  # early exit, big boy found, we cant find antying else, we should just leave...
            # if (l,r) in dp: return dp[(l,r)] # dont need dp because we are on big to small grind
            if isPalandrome(l,r):
                res = s[l:r+1]
                return
            # we want to try both options next
            recurse(l+1, r)
            recurse(l,r-1)
        
        recurse(0,len(s)-1)
        return res