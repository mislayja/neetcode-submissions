# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:


    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        last = None
        curr = head

        while curr!=None:
            # grab next so we can assign later
            temp = curr.next

            # point current to last one
            curr.next = last

            # update state for next iteration
            last = curr
            curr = temp

        # curr was updated to null,
        # last is head 
        return last

        
        