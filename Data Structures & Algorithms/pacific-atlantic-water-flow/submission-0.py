# class Solution:
#     def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
#         # this is phrased as graph...,
#         # it sounds like for every tile we need to check if it will flow into both, and store that information somehow...
#         # likely a cache where tile -> pacific/atlantic, and we would recursively compute it as we iterate across entire list adding the tiles.
#         cache = {}
#         # the values will be in the form of pacific, atlantic, pend, both, none
#         # if we see a pending we'll skip for now

        
#         ROWS, COLS = len(heights), len(heights[0])

#         def dfs(row, col):
#             height = heights[row][col]
#             cache[(row,col)] = "pending"
#             touches_pacific = False
#             touches_atlantic = False
#             # ok we need to check for which values are <= current, and
#             for delta_r, delta_c in ((0,1),(0,-1),(1,0),(-1,0)):
#                 next_row, next_col = row+delta_r, col+delta_c
#                 if next_row <0 or next_col <0:
#                     touches_pacific=True
#                     continue
#                 elif next_row>=ROWS or next_col>=COLS:
#                     touches_atlantic=True
#                     continue
                    
#                 # valid spot now
#                 elif heights[next_row][next_col] <= height:
#                     # ok lets check if it's in the map, if so we need to check if it touches pacific or atlantic, or both
#                     if (next_row, next_col) not in cache:
#                         dfs(next_row, next_col)
#                     # weve populated it now, let's check what it's got
#                     string = cache[(next_row, next_col)]
#                     if string in ("both", "atlantic"):
#                         touches_atlantic=True
#                     if string in ("both","pacific"):
#                         touches_pacific=True
                        
            
#             # resolve now
#             if touches_pacific and touches_atlantic:
#                 cache[(row, col)]= "both"
#             elif touches_atlantic:
#                 cache[(row, col)]="atlantic"
#             elif touches_pacific:
#                 cache[(row, col)]="pacific"
#             else:
#                 cache[(row, col)]="none"
#             print(f"node=({row},{col})= {cache[(row, col)]}")

        
#         res = []
#         for row in range(ROWS):
#             for col in range(COLS):
#                 if (row, col) not in cache:
#                     dfs(row,col)
#                 if cache[(row, col)] == "both":
#                     res.append((row, col))
#         return res
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        pac, atl = set(), set()
        
        def dfs(row, col, visit, prevHeight):
            if ((row,col) in visit or
                row<0 or col<0 or row>=ROWS or col>=COLS or
                heights[row][col] < prevHeight):
                return 
            visit.add((row,col))
            dfs(row+1,col,visit,heights[row][col])
            dfs(row-1,col,visit,heights[row][col])
            dfs(row,col+1,visit,heights[row][col])
            dfs(row,col-1,visit,heights[row][col])

        for c in range(COLS):
            dfs(0,c,pac,heights[0][c])
            dfs(ROWS-1,c, atl, heights[ROWS-1][c])
        for r in range(ROWS):
            dfs(r,0, pac, heights[r][0])
            dfs(r,COLS-1, atl, heights[r][COLS-1])
        res = []
        for r in range(ROWS):
            for c in range(COLS):
                if (r,c) in pac and (r,c) in atl:
                    res.append((r,c))
        return res

