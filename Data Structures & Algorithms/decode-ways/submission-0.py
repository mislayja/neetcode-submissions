class Solution:
    def numDecodings(self, s: str) -> int:
        # this is dp because we need to figure out the ways we can decode
        # i dont really understand how this ids dynamic probtramming? 
        total = 0
        r = len(s)-1
        # dp ={}
        def count(l):
            if l>r:
                nonlocal total
                total+=1
                return
            if s[l] == "0": return
            elif s[l] == "1":
                count(l+2)
            elif s[l] == "2":
                # only when 2nd digit is within
                if l+1 <=r and s[l+1] in "0123456":
                    count(l+2)
            count(l+1)
            
            
        
        # we really only need to know left, right is always known

        count(0)
        return total