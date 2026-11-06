class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        # iterate though tracking # of diferences and if characters overall are diferent? 
        chars = [0]*26
        diff_count = 0
        for idx in range(len(s1)):
            chars[ord(s1[idx])-ord('a')]+=1
            chars[ord(s2[idx])-ord('a')]-=1
            if s1[idx]!=s2[idx]: diff_count+=1
        # print(chars)
        return diff_count<=2 and max(chars)==0