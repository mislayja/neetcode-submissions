class Solution:

    def encode(self, strs: List[str]) -> str:
        # we need a seperator that will work regardless of which character is used as seperator
        # I could just prepend each character with some delim and 
        # use number for length of string...
        s = ""
        for string in strs:
            l = len(string)
            s += (str(l)+"#"+string)
        return s



    def decode(self, s: str) -> List[str]:
        ret = []

        idx = 0
        while idx < len(s):
            size = ""
            i = 0
            while s[idx+i].isdigit():
                size+=s[idx+i]
                i+=1
            # at this point, idx points to 1st char in number,
            # idx+i points to "#", one past this is where word is
            start = idx+i+1
            ret.append(s[start:start+int(size)])
            idx = start+int(size)
        return ret

            
