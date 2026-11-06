class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # create dp array
        dp = [[0]*n for _ in range(m)]
        # print(dp)

        # set bottom row=-1
        for i in range(n):
            dp[0][i]=1
        # set right row=1
        for i in range(m):
            dp[i][0] = 1
        
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]

        # from bottom up

        return dp[m-1][n-1]