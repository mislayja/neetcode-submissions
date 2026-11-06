# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        # fine lets use recursion

        def recurse(node):
            # we want to return the value of the valid/None Node, 
            if node == None: return None

            # we want to check if this node is valid...
            if node.val == val: return recurse(node.next)
            return node

        head = recurse(head)


        if head != None:
            node = head
            while node != None and node.next != None:
                node.next = recurse(node.next)
                node = node.next

        return head