class Solution {
    fun isPalindrome(s: String): Boolean {
        val probS = s.filter { it.isLetterOrDigit() }.lowercase()

        var l = 0
        var r = probS.length-1
        while (l < r){
            if (probS[l] != probS[r]){return false}
            l++
            r--
        }
        return true
    }
}
