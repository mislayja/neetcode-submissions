class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        # need count of every character % total = 0
        arr = [0]*26
        for word in words:
            for char in word:
                arr[ord(char)-97]+=1

        l = len(words)
        for count in arr:
            if count %l !=0: return False

        return True

        