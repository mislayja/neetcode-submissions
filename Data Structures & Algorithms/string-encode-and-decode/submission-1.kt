class Solution {

    fun encode(strs: List<String>): String {
        var s = ""
        for (str in strs){
            s +="${str.length}#$str"
        }
        return s
    }

    fun decode(str: String): List<String> {
        val res = mutableListOf<String>()
        var idx = 0
        while (idx < str.length){
            var s = ""
            while(str[idx]!='#'){
                s+=str[idx]
                idx+=1
            }
            // we have string size here, idx points to # character
            idx+=1
            val string_length = s.toInt()
            res.add(str.slice(idx..idx+string_length-1))
            idx+=string_length
        }
        return res
    }
}
