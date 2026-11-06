# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: ListNode | None) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head or not head.next: 
            return
        

        # intuition, we reverse 2nd half of list using 2 pointer to get 1/2 mid point
        # we can then iterate on the list...
        slow = head
        fast = head
        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next
        
        # print(f"slow={slow.val}, fast={fast.val}")
        # slow = mid point here
        last = None
        while slow:
            temp = slow.next
            slow.next = last
            last = slow
            slow = temp
        
        # last is start of reversed :)
        # now we have two lists which have the middle node point to None
        # we need to zipper them up

        while head or last:
            if head and last:
                next_head = head.next
                next_last = last.next
                head.next = last
                last.next = next_head
                head= next_head
                last=next_last
            else:
                break
        