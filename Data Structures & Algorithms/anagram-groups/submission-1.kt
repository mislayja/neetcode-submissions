class Solution {
    fun groupAnagrams(strs: Array<String>): List<List<String>> {
        val map = HashMap<List<Int>, MutableList<String>>()

        for (str in strs){
            val temp = IntArray(26)
            for (c in str){
                temp[c-'a']++
            }
            val tempList = temp.toList()
            val list = map.getOrPut(tempList) {mutableListOf()}
            list.add(str)
        }
        return map.values.toList()
    }
}