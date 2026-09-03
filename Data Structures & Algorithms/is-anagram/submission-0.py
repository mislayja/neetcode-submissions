
from collections import defaultdict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # we can use hashmap
        # do comparison after the fact...
        l =defaultdict(int)
        r = defaultdict(int)
        for char in s:
            l[char]+=1
        for char in t:
            r[char]+=1
        
        return l == r

        