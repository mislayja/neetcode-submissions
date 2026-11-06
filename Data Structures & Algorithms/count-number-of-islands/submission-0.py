class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # we can mark seen by setting values to 0

        ROWS, COLS = len(grid), len(grid[0])

        # recursively consume/marke the island as seen
        def consumeIsland(r,c):
            for delta_r, delta_c in ((1,0),(-1,0),(0,1),(0,-1)):
                next_r, next_c = r+delta_r, c+delta_c
                if next_r<0 or next_c<0 or next_r>=ROWS or next_c>=COLS: 
                    continue
                if grid[next_r][next_c] == "1":
                    grid[next_r][next_c] = "0"
                    consumeIsland(next_r, next_c)



        # iterate through each spot, when we find and island we will consume the entire thing
        # ie the next slot that was and island wont look like one anymore. 
        total = 0
        for r in range(ROWS):
            for c in range(COLS): 
                if grid[r][c] =="1":
                    total+=1
                    consumeIsland(r,c)
                    # print(grid)

        return total