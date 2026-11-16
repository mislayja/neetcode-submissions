class Solution {
    fun maxProfit(prices: IntArray): Int {
        var res = 0
        var low = prices[0]
        for (price in prices){
            res = maxOf(res, price-low)
            low = minOf(low, price)
        }
        return res
    }
}
