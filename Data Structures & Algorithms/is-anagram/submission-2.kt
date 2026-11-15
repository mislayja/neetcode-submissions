class Solution {
    fun isAnagram(s: String, t: String): Boolean {
        val counts = IntArray(26)
        for (c in s){
            counts[c-'a']++
        }
        for (c in t){
            counts[c-'a']--
        }
        return counts.all { it == 0 }
    }
}