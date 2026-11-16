/**
 * Definition for singly-linked list.
 * class ListNode(var `val`: Int) {
 *     var next: ListNode? = null
 * }
 */

class Solution {
    fun reverseList(head: ListNode?): ListNode? {
        if (head == null){return head}
        var last: ListNode? = null
        var curr = head

        while (curr != null){
            val temp = curr.next
            curr.next = last
            last = curr
            curr = temp
        }
        return last
    }
}
