

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # brute force would be check prefix for all words in word for s, remove and recurse down string.  Maybe memoization
        dp = {"":True}
        
        def dfs(s):
            if s in dp: return dp[s]
            for word in wordDict:
                if s.startswith(word) and dfs(s[len(word):]):
                    dp[s] = True
                    return True
            dp[s]=False
            return False
        return dfs(s)


