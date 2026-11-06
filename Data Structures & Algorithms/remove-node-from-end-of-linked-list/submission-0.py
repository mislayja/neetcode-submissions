# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode | None, n: int) -> ListNode | None:
        start = ListNode(next=head)
        back = start
        curr = head

        # we only want to increment our back to point to nth node
        while curr:
            n-=1
            if n<0:
                back = back.next
            curr = curr.next
        # print(f"back={back.val}")

        # edge case for start where returning head is incorrect
        if back == start:
            return back.next.next
        
        # remove node from LL, by just moving next pointers.
        back.next = back.next.next
        return head
                
        
        