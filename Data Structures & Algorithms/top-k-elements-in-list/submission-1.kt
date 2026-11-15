class Solution {
    fun topKFrequent(nums: IntArray, k: Int): IntArray {
        val hash = HashMap<Int, Int>()
        for (num in nums){
            hash[num] = hash.getOrDefault(num,0)+1
        }
        // iterate on hashmap values+frequencies
        val buckets = List<MutableList<Int>>(nums.size+1) {mutableListOf<Int>()}
        for ((num, freq) in hash){
            buckets[freq].add(num)
        }
        // the answer is always unique, not that the frequencies are unique...

        // we can 1 pass -> hash the frequencies
        // pass2 -> buckets up to len nums
        // reverse iterate on nums

        val res = IntArray(k)
        var idx = 0
        for (i in buckets.indices.reversed()){
            val bucket = buckets[i]
            if (bucket != null) {
                // add to res here
                for (num in bucket){
                    res[idx]=num
                    idx++
                }
            }
            if (idx==k){break}
        }
        return res
    }
}
