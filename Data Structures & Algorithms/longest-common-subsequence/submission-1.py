# class Solution:
#     def longestCommonSubsequence(self, text1: str, text2: str) -> int:
#         dp = {}
#         res = 0

#         def dfs(t1, t2):
#             if (t1, t2) in dp: return dp[(t1,t2)]
#             if t1>=len(text1) or t2>=len(text2): return 0

#             if text1[t1]==text2[t2]: 
#                 # increment both +call, +memoize it + return it
#                 ret = dfs(t1+1, t2+1)
#                 dp[(t1,t2)] = ret+1
#                 return ret+1
#             # we call both and update based on max
#             ret = max(dfs(t1+1,t2), dfs(t1,t2+1))
#             dp[(t1,t2)] = ret
#             return ret

#         return dfs(0,0)


# bottom up is faster? 
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = [[0 for j in range(len(text2) + 1)]
                 for i in range(len(text1) + 1)]

        for i in range(len(text1) - 1, -1, -1):
            for j in range(len(text2) - 1, -1, -1):
                if text1[i] == text2[j]:
                    dp[i][j] = 1 + dp[i + 1][j + 1]
                else:
                    dp[i][j] = max(dp[i][j + 1], dp[i + 1][j])

        return dp[0][0]