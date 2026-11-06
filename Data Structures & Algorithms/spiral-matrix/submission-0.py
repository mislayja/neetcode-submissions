class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        l,top,bottom,r = 0,0,len(matrix),len(matrix[0])
        res = []

        
        while l < r and top < bottom:
            
            # grap top row now
            for i in range(l,r):
                res.append(matrix[top][i])
            top+=1
            
            # grab vertical row now
            for i in range(top,bottom):
                res.append(matrix[i][r-1])
            r-=1

            # check if pointers have crossed now
            if not (l<r and top<bottom):
                break

            # bottom row now
            for i in range(r-1,l-1,-1):
                res.append(matrix[bottom-1][i])
            bottom-=1

            # left row now
            for i in range(bottom-1,top-1,-1):
                res.append(matrix[i][l])
            l+=1

        return res