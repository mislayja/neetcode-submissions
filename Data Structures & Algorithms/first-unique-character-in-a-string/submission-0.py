class Solution:
    def firstUniqChar(self, s: str) -> int:
        x = {}
        for char in s:
            if char not in x:
                x[char]=0
            x[char]+=1
        for idx, char in enumerate(s):
            if x[char]==1:
                return idx

        return -1