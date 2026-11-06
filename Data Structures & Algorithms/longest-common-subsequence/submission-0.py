class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = {}
        res = 0

        def dfs(t1, t2):
            if (t1, t2) in dp: return dp[(t1,t2)]
            if t1>=len(text1) or t2>=len(text2): return 0

            if text1[t1]==text2[t2]: 
                # increment both +call, +memoize it + return it
                ret = dfs(t1+1, t2+1)
                dp[(t1,t2)] = ret+1
                return ret+1
            # we call both and update based on max
            ret = max(dfs(t1+1,t2), dfs(t1,t2+1))
            dp[(t1,t2)] = ret
            return ret

        return dfs(0,0)