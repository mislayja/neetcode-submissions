class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        ret = -1

        tracker = {}
        # we can iterate on this using a dict and track last time it was seen
        for idx, char in enumerate(s):
            if char in tracker:
                diff = tracker[char]
                ret = max(ret, idx-diff-1)
            tracker[char]= idx
        return ret