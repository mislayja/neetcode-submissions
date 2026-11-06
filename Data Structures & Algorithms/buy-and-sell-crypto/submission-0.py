class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        low = None
        high = None
        res = 0
        for idx in range(len(prices)-1, -1, -1):
            # we look at high first
            if high:
                # need to know if new high
                if prices[idx] >= high:
                    low=None
                    high= prices[idx]
                else:
                    # check now now if we have new res
                    if low:
                        low = min(low, prices[idx])
                        res = max(res, high-low)
                        # print(f"new low found, low:{low}, high:{high}")
                    else: 
                        # we know its lower,
                        low = prices[idx]
                        res = max(high-low, res)

            else:
                high = prices[idx]
        # we couldve done this right toleft just keeping track of min trying tocompute max at each pass
        # both O(n), not the worst, just a couple more checks than needed :)
                



        return res

