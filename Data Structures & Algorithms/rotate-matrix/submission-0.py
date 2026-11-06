class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        # we at most need to rotate 4 items at a time, we jsut need to be able to iterate in a way that lets us know which indeces to start at 
        # 2x2 = 1
        # 3x3 = 2
        # 4x4 = 3+1 for inner...
        l,r = 0, len(matrix)-1

        while l < r: 
            for i in range(r-l):
                top,bottom = l, r # sware matrix

                # save top left. 
                temp = matrix[top][l+i]
                
                # move bottom left into top left
                matrix[top][l+i] = matrix[bottom-i][l]

                # move bottom right into bottom left
                matrix[bottom-i][l]=matrix[bottom][r-i]

                # mvoe top right into bottom right
                matrix[bottom][r-i]=matrix[top+i][r]

                # finally savt temp into top right
                matrix[top+i][r] = temp
            l+=1
            r-=1
        