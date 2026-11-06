class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) <= 1: return len(s)
         
        l = 0
        r = 0
        
        d = {}
        
        ret = 1
        while r<len(s):
            if s[r] in d:
                # we need to update left here
                idx = d[s[r]]
                while l<=idx:
                    del d[s[l]]
                    l+=1
            else:
                
                d[s[r]] = r
                ret = max(ret, r-l+1)
                # print(f"d={d}, r={r},l={l}")
                r+=1
                
                
            
        return ret