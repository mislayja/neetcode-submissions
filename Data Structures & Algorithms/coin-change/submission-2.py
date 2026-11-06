class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # lets sort coins so we can move from right to left to make up total
        coins.sort()

        # lets try to do this with dp first
        dp = {}
        # dp will hold the {amt: min coins needed}
        res = 0

        def numCoins(amt, idx):
            # print(f"amt={amt}, idx={idx}")
            if amt in dp: return dp[amt]
            if amt == 0: return 0
            
            low = 10001
            for val in range(idx,-1,-1):
                # we will call numCoins here, and record minimum for the current amt when done
                if coins[val]<=amt:
                    temp = numCoins((amt-coins[val]),val)
                    if temp !=-1:
                        low = min(low, 1+ temp)

            if low == 10001:
                low = -1
            # print(f"amt={amt}, idx={idx}, low={low}")
            dp[amt] = low
            return low

        res = numCoins(amount, len(coins)-1)
        return res