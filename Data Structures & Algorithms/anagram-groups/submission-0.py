from collections import defaultdict

# class Solution:
#     def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
#         # could just create dictionary for each string char-># of char
#         # return values for each one...
#         d = defaultdict(list)

#         for string in strs:
#             tmp = defaultdict(int)
#             for char in string:
#                 tmp[char]+=1
#             d[tuple(sorted(tmp.items()))].append(string)

#         return list(d.values())


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:    
        ans = defaultdict(list)

        for s in strs:
            count = [0] * 26

            for c in s:
                count[ord(c) - ord("a")] += 1
            ans[tuple(count)].append(s)
        
        return list(ans.values())


# third solution involves keying by sorted string, this is also valid.
