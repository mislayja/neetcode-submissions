class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        # 2 pass, record all 0's this is not 0(1)...
        ROW,COL = len(matrix),len(matrix[0])
        # top row 0
        top_row=False

        for i in range(ROW):
            for j in range(COL):
                if matrix[i][j]==0:
                    if i ==0:
                        top_row=True
                        # set col too
                        matrix[0][j]=0
                    else: 
                        matrix[i][0] = 0
                        matrix[0][j] = 0
        
        # print(f"matrix={matrix},top_row={top_row}")

        # pass 2, we track 0th spot for every idx, check if 0 and update...
        # skip 1st row because we do it last.
        for i in range(1, ROW):
            for j in range(1, COL):
                if matrix[0][j]==0 or matrix[i][0]==0:
                    matrix[i][j]=0
        
        # do 1st col last because we would 0 everything out uneccesarily otherwise. 
        if matrix[0][0] ==0:
            for i in range(ROW):
                matrix[i][0] = 0
        
        # finally check 1st row with seperate bool
        if top_row:
            for j in range(COL):
                matrix[0][j] = 0
            