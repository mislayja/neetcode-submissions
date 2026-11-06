class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        # I didn th_ReturnT_co_nd, is already :):)
        l = len(grid[0])
        count = [0]*(l*l)

        for inner in grid:
            for val in inner:
                count[val-1]+=1
        ret = [0,0]
        # print(count)
        for idx, total in enumerate(count):
            if total == 0: # missing 
                # print(f"assigning missing={idx+1}")
                ret[1]=idx+1
            if total == 2: # doplicated
                # print(f"assigning duplicated={idx+1}")
                ret[0]=idx+1

        return ret
