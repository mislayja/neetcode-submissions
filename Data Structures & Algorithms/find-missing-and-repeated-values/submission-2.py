from collections import defaultdict
class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        d = defaultdict(int)

        for row in grid:
            for item in row:
                d[item]+=1
        
        ret = [0,0]
        for val in range(1, len(grid)*len(grid)+1):
            if d[val]==0:
                ret[1]=val
            if d[val]==2:
                ret[0]=val
        return ret