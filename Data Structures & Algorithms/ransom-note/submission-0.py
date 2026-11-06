class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        # 1 array, count up from magazine
        # decrement from ransomNote, if <0 return false
        # return true otherwise
        alphabet = [0]*26
        for char in magazine:
            alphabet[ord(char)-ord('a')]+=1
        for char in ransomNote:
            alphabet[ord(char)-ord('a')]-=1
            if alphabet[ord(char)-ord('a')] <0: return False
        return True
        